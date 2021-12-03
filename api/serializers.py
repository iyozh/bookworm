from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.models import Shop

User = get_user_model()


class ShopSerializer(ModelSerializer):
    """ShopSerializer transforms shop data into json format
    Serializable fields: name, creator"""

    creator = serializers.ReadOnlyField(source="creator.username")

    class Meta:
        model = Shop
        fields = [
            "name",
            "creator",
        ]


class UserSerializer(ModelSerializer):
    """UserSerializer transforms shop data into json format
    Serializable fields: username, password, password2(confirm field)"""

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "password2",
        ]

    def validate(self, attrs):
        """This method validates if passwords are equal. Otherwise method throws ValidationError"""
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        """Create method creates user instance and sets the user’s password to the given raw string, taking care of
        the password hashing. Saves and return user instance"""
        user = User.objects.create(
            username=validated_data["username"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
