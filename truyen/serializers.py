from rest_framework import serializers
from .models import Truyen


class TruyebSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
