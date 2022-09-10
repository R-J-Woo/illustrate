from rest_framework import serializers
from users.models import Profile
from users.serializers import ProfileSerializer
from .models import Illustrates


class IllustSerializer(serializers.ModelSerializer):  # 일러스트 정보 가져오는 serializer
    profile = ProfileSerializer(read_only=True)  # nested serializer

    class Meta:
        model = Illustrates
        fields = ('pk', 'profile', 'image', 'title', 'description', 'category',
                  'purchase_number', 'likes', 'price', 'register_date')


class IllustCreateSerializer(serializers.ModelSerializer):  # 일러스트 등록 serializer
    class Meta:
        model = Illustrates
        fields = ('image', 'title', 'description', 'price', 'category')
