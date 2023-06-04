from rest_framework import pagination, viewsets

from ads.models import Ad, Comment

from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    pass


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializers = {"list": AdSerializer, "retrive: AdDetailSerializer"}
    default_serializer = AdDetailSerializer

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
