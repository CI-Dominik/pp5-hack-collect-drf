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

    def get_cleaned_data(self):
        # Get all data for cleaned registration
        data = super().get_cleaned_data()

        # Ensure the fields are present in the cleaned data
        data['username'] = self.validated_data.get('username', '')
        data['email'] = self.validated_data.get('email', '')
        data['password1'] = self.validated_data.get('password1', '')
        data['password2'] = self.validated_data.get('password2', '')
        data['first_name'] = self.validated_data.get('first_name', '')
        data['last_name'] = self.validated_data.get('last_name', '')
        return data
