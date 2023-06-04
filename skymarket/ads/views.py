from rest_framework import pagination, viewsets, generics

from ads.models import Ad, Comment

from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    pass


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializers = {"list": AdSerializer, "retrieve": AdDetailSerializer}
    default_serializer = AdDetailSerializer

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)


class CommentViewSet(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(ad=self.kwargs['id'])
