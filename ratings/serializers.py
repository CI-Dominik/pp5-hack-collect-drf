from rest_framework import serializers
from django.db import IntegrityError
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Rating
        fields = [
            'id',
            'user',
            'hack',
            'rating',
            'created_at',
            'updated_at',
            ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'Possible duplicate'})
