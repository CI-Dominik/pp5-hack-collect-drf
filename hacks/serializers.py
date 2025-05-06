from rest_framework import serializers
from .models import Hack
from ratings.models import Rating
from categories.serializers import CategorySerializer


class HackSerializer(serializers.ModelSerializer):
    """
    Hack Serializer to return JSON data.
    Profile image gotten from the profile itself is verified to
    no exeed the given limits.
    "is_owner" is used to determine if the current user is
    the Hack's owner.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    rating_id = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    average_rating = serializers.FloatField(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)
    category = CategorySerializer

    # Validate image size and dimensions

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size is larger than 2 '
                                              'megabytes, please choose a '
                                              'smaller image!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height is larger than 4096 pixels, '
                'please choose a smaller image!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width is larger than 4096 pixels, '
                'please choose a smaller image!'
            )
        return value

    # Check if the current user is the owner of the hack

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # Check if the Hack was rated

    def get_rating_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            rating = Rating.objects.filter(
                owner=user, hack=obj
            ).first()
            return rating.id if rating else None
        return None

    class Meta:
        model = Hack
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'created_at',
            'updated_at',
            'title',
            'content',
            'image',
            'category',
            'average_rating',
            'comments_count',
            'rating_id',
        ]
