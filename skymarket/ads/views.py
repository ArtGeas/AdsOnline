from rest_framework import pagination, viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdDetailSerializer, AdCreateSerializer, CommentSerializer, CommentCreateSerializer
from ads.filters import AdFilter
from ads.permissions import IsOwner, IsStaff


class AdPagination(pagination.PageNumberPagination):
    page_size = 4
    page_query_param = "page_size"



# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    # pagination_class = AdPagination

    filter_backends = (DjangoFilterBackend, )
    filterset_class = AdFilter

    serializers = {"list": AdSerializer, "retrieve": AdDetailSerializer, "create": AdCreateSerializer}
    default_serializer = AdDetailSerializer

    default_permission = [AllowAny]
    permissions = {
        'retrieve': [IsAuthenticated],
        'create:': [IsAuthenticated],
        'update': [IsOwner | IsStaff],
        'destroy': [IsOwner | IsStaff],
        'partial_update': [IsOwner | IsStaff]
    }

    def get_permissions(self):
        self.permission_classes = self.permissions.get(self.action, self.default_permission)
        return super().get_permissions()

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def create(self, request, *args, **kwargs):
        request.data['author'] = request.user.id
        return super().create(request, *args, **kwargs)

    @action(detail=False, methods=["get"])
    def me(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

    permissions = {
        'retrieve': [IsAuthenticated],
        'create:': [IsAuthenticated],
        'update': [IsOwner | IsStaff],
        'destroy': [IsOwner | IsStaff],
        'partial_update': [IsOwner | IsStaff]
    }
    default_permission = [AllowAny]

    serializers = {
        'create': CommentCreateSerializer,
    }
    default_serializer = CommentSerializer

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        self.permission_classes = self.permissions.get(self.action, self.default_permission)
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        data = {
            'ad': self.kwargs.get('ad_pk'),
            'author': request.user.pk,
            'text': request.data.get('text')
        }

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
