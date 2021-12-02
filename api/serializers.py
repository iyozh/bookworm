from django.contrib.auth import get_user_model, validators
from rest_framework import serializers, exceptions
from rest_framework.serializers import ModelSerializer

from api.models import Shop

User = get_user_model()


class ShopSerializer(ModelSerializer):
    """ShopSerializer transforms shop data into json format
    Serializable fields: name"""

    class Meta:
        model = Shop
        fields = [
            "name",
        ]
