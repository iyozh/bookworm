from rest_framework import permissions
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    ListAPIView,
)
from django.contrib.auth import get_user_model
from api.models import Shop, Book
from api.permissions import IsOwnerOrReadOnly, IsOwnerOfShopOrReadOnly
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
    """This view is responsible for getting data about books of current shop by shop_id received from url endpoint"""
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOfShopOrReadOnly]

    def get_queryset(self):
        """This method allows getting queryset of books of the single shop"""
        queryset = Book.objects.filter(shop_id=self.kwargs.get("pk"))
        return queryset

    """This method save the book instance and match it with specified shop"""
    def perform_create(self, serializer):
        serializer.save(shop_id=self.kwargs.get("pk"))


class BookRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """This view is responsible for getting data about single book and realizes functionality of updating/deleting
    books."""

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
