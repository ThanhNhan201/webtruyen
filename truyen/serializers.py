from rest_framework import serializers
from .models import Truyen, Comment, Rate


class TruyenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truyen
        fields = (
            'id',
            'name',
            'author',
            'category',
            'views',
            # 'rating',
            'updated_at',
            'follow_up',
            'number_of_comment',
        )

class TruyenDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truyen
        fields = (
            'id',
            'name',
            'author',
            'category',
            'is_completed',
            'views',
            'rating',
            'created_at',
            'updated_at',
            'follow_up',
            'content',
            # 'number_of_comment',
            'removed',
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'truyen',
            'user',
            'comment',
            'created_at',
            'update_at',
            'removed',
        )

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'truyen',
            'user',
            'rate',
            'created_at',
            'update_at',
            'removed',
        )