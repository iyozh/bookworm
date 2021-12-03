from rest_framework import permissions, status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)
from django.contrib.auth import get_user_model
from rest_framework.response import Response

from api.models import Shop
from api.serializers import ShopSerializer, UserSerializer

User = get_user_model()


class ShopListView(ListCreateAPIView):
    """This view is responsible for getting data about shops and realizes functionality of creating shop"""

    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Method is responsible for creating shop and matching it with current user"""

        serializer.save(creator=self.request.user)


class ShopRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """This view is responsible for getting data about single shop and realizes functionality of updating/deleting
    shops."""

    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        """Method deletes shop that belongs to current user. If it doesn't exist method will throw ValidationError"""

        shop = Shop.objects.filter(pk=self.kwargs.get("pk"), creator=self.request.user)
        if shop.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError("This isn't your shop to delete")

    def update(self, request, *args, **kwargs):
        """Method updates shop that belongs to current user.If it doesn't exist method will respond with error
        message and status code 400"""

        shop = Shop.objects.filter(pk=self.kwargs.get("pk"), creator=self.request.user)
        if shop.exists():
            serializer = ShopSerializer(shop.first(), data=request.data, partial=True)
            if serializer.is_valid():
                shop = serializer.save()
                return Response(ShopSerializer(shop).data)
        return Response(
            {"error": "Shop doesn't belong to you or data is incorrect"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class Register(CreateAPIView):
    """Register view for signing up."""

    serializer_class = UserSerializer
