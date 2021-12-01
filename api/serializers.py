from rest_framework.serializers import ModelSerializer

from api.models import Shop


class ShopSerializer(ModelSerializer):
    """ShopSerializer transforms shop data into json format
    Serializable fields: name"""

    class Meta:
        model = Shop
        fields = [
            "name",
        ]
