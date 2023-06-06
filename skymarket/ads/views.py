from rest_framework import pagination, viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer
from ads.filters import AdFilter
from ads.permissions import IsOwner, IsStaff


class AdPagination(pagination.PageNumberPagination):
    page_size = 4
    page_query_param = "page_size"



# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination

    filter_backends = (DjangoFilterBackend, )
    filterset_class = AdFilter

    serializers = {"list": AdSerializer, "retrieve": AdDetailSerializer}
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


class CommentViewSet(generics.ListAPIView):
    serializer_class = CommentSerializer

    permissions = {
        'retrieve': [IsAuthenticated],
        'create:': [IsAuthenticated],
        'update': [IsOwner | IsStaff],
        'destroy': [IsOwner | IsStaff],
        'partial_update': [IsOwner | IsStaff]
    }

    def get_permissions(self):
        self.permission_classes = self.permissions.get(self.action)
        return super().get_permissions()

    def get_queryset(self):
        return Comment.objects.filter(ad=self.kwargs['id'])
