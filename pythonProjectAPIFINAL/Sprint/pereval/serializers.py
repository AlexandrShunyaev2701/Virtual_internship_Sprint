from .models import *
from rest_framework import serializers
from rest_framework.serializers import ValidationError


class UserSerializer(serializers.ModelSerializer):

     class Meta:
        model = User
        fields = [
            'email', 'phone', 'first_name', 'last_name',
            'surname'
        ]

class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = [
            'latitude', 'longtitude', 'height'
        ]


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'title', 'image'
        ]


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = [
            'winter', 'summer', 'autumn', 'spring'
        ]

class PerevalSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coord = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer()

    class Meta:
        model = Pereval
        fields = [
            'pk', 'status', 'beauty_title', 'title', 'other_titles',
            'connect', 'user', 'coord', 'level', 'images'
        ]

    def create(self, validated_data):

        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)

        coord_data = validated_data.pop('coord')
        coord = Coords.objects.create(**coord_data)

        level_data = validated_data.pop('level')
        level = Level.objects.create(**level_data)

        images_data = validated_data.pop('images')
        images = Image.objects.create(**images_data)

        pereval = Pereval.objects.create(**validated_data, user=user, coord=coord, level=level, images=images)
        return pereval

    def update(self, instance, validated_data):
        instance.user = validated_data.get(Pereval.user, instance.user)
        instance.coord = validated_data.get(Pereval.coord, instance.coord)
        instance.level = validated_data.get(Pereval.level, instance.level)
        instance.images = validated_data.get(Pereval.images, instance.images)
        instance.status = validated_data.get('status', instance.status)
        instance.beauty_title = validated_data.get('beauty_title', instance.beauty_title)
        instance.title = validated_data.get('title', instance.title)
        instance.other_titles = validated_data.get('other_titles', instance.other_titles)
        instance.connect = validated_data.get('connect', instance.connect)
        instance.save()
        return instance

    def validate(self, attrs):
        user_data = attrs.get('user')
        if not user_data:
            raise ValidationError("User data is missing.")

        if self.instance:
            user = self.instance.user
        else:
            try:
                user = User.objects.get(email=user_data.get('email'))
            except User.DoesNotExist:
                user = None

        if user is not None:
            if user.first_name != user_data.get('first_name') or \
                    user.last_name != user_data.get('last_name') or user.surname != user_data.get('surname') or \
                    user.phone != user_data.get('phone'):
                raise ValidationError("Информация не может быть изменена")

        super().validate(attrs)

        return attrs



