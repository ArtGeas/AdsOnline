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
        fields = "__all__"

    def create(self, validated_data):
        author_id = validated_data.pop('author_id')
        # author = User.objects.get(id=author_id)

        new_ad = Ad.objects.create(author_id=author_id, **validated_data)
        return new_ad


class AdDetailSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    class Meta:
        model = Ad
        fields = "__all__"
