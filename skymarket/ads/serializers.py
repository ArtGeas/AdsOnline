from rest_framework import serializers

from ads.models import Ad, Comment
from users.models import User


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    author_first_name = serializers.CharField(source='author.first_name')
    author_last_name = serializers.CharField(source='author.last_name')
    author_image = serializers.ImageField(source='author.image')
    author_id = serializers.IntegerField(source='author.id')
    ad_id = serializers.IntegerField(source='ad.id')

    class Meta:
        model = Comment
        fields = ["pk", "text", "author_id", "created_at",
                  "author_first_name", "author_last_name", "ad_id", "author_image"]


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class AdSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'price', 'description']


class AdDetailSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели

    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')

    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'price', 'description',
                  'author_id', 'author_first_name', 'author_last_name']


class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'
