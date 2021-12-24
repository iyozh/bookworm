from django.urls import path
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.views import BookRetrieveUpdateDestroyView

urlpatterns = [
    path("shops/", views.ShopListView.as_view(), name="shops"),
    path(
        "shops/<int:pk>",
        views.ShopRetrieveUpdateDestroyView.as_view(),
        name="detail_shop",
    ),
    path("books/", views.BooksListView.as_view(), name="books"),
    path(
        "shops/<int:pk>/books",
        views.BooksForCurrentShopListView.as_view(),
        name="shop_books",
    ),
    path("books/<int:pk>", BookRetrieveUpdateDestroyView.as_view(), name="detail_book"),
    # AUTH
    path("signup/", views.Register.as_view(), name="signup"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
