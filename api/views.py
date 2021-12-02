from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model
from api.models import Shop
from api.serializers import ShopSerializer

User = get_user_model()


class ShopListView(ListCreateAPIView):
    """This view is responsible for getting data about shops and realizes functionality of creating shop"""

    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ShopRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """This view is responsible for getting data about single shop and realizes functionality of updating/deleting
    shops."""

    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
