from rest_framework import serializers
from .models import Hack


class HackSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    average_rating = serializers.FloatField(read_only=True)

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
        ]
