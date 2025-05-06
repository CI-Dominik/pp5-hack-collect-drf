from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """
    Serializer for the current user.
    The username gets checked for length.
    """
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image', 'is_staff'
        )

    def validate_username(self, value):
        if len(value) > 15:
            raise serializers.ValidationError(
                "Username must be at most 15 characters long."
                )
        return value


class CustomRegisterSerializer(RegisterSerializer):
    """
    Validation for the username when registering.
    """

    def validate_username(self, value):
        if len(value) > 15:
            raise serializers.ValidationError(
                "Username must be at most 15 characters long."
                )
        return value
