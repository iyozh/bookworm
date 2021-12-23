from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework import permissions
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView, ListAPIView,
)
from django.contrib.auth import get_user_model
from api.models import Shop, Book
from api.permissions import IsOwnerOrReadOnly
from api.serializers import ShopSerializer, UserSerializer, BookSerializer

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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class Register(CreateAPIView):
    """Register view for signing up."""

    serializer_class = UserSerializer


class BooksListView(ListAPIView):
    """This view is responsible for getting data about all existing books"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BooksForCurrentShopListView(ListCreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Book.objects.filter(shop_id=self.kwargs.get("pk"))
        return queryset

    def perform_create(self, serializer):
        serializer.save(shop_id=self.kwargs.get("pk"))
