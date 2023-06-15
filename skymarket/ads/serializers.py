from rest_framework import serializers

from ads.models import Ad, Comment
from users.models import User


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    class Meta:
        model = Comment
        fields = "__all__"


class AdSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    class Meta:
        model = Ad
        fields = ['id', 'image', 'title', 'price', 'description']


class AdDetailSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели

    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')

    class Meta:
        model = Ad
        fields = ['id', 'image', 'title', 'price', 'phone', 'description',
                  'author_id', 'author_first_name', 'author_last_name']
