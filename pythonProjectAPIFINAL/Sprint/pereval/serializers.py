from .models import *
from rest_framework import serializers



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
        instance.coord = validated_data.get('coord', instance.coord)
        instance.level = validated_data.get('level', instance.level)
        instance.image = validated_data.get('image', instance.image)
        instance.status = validated_data.get('status', instance.image)
        instance.beauty_title = validated_data.get('beauty_title', instance.beauty_title)
        instance.title = validated_data.get('title', instance.title)
        instance.other_titles = validated_data.get('other_titles', instance.other_titles)
        instance.connect = validated_data.get('connect', instance.connect)
        instance.save()
        return instance



