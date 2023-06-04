from rest_framework import pagination, viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend

from ads.models import Ad, Comment

from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer
from ads.filters import AdFilter


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

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)


class CommentViewSet(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(ad=self.kwargs['id'])
