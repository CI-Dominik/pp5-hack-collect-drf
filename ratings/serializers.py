from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    """
    Checks if a rating was already left by the current user.
    If not, a new one is created.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Rating
        fields = [
            'id',
            'owner',
            'hack',
            'rating',
            'created_at',
            'updated_at',
            ]

    def create(self, validated_data):
        try:
            rating = Rating.objects.get(
                owner=self.context['request'].user,
                hack=validated_data['hack']
                )
            rating.rating = validated_data['rating']
            rating.save()
            return rating
        except Rating.DoesNotExist:
            validated_data['owner'] = self.context['request'].user
            return super().create(validated_data)
