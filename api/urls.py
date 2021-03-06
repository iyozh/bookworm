from django.urls import path
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("shops/", views.ShopListView.as_view(), name="shops"),
    path(
        "shops/<int:pk>",
        views.ShopRetrieveUpdateDestroyView.as_view(),
        name="detail_shop",
    ),
    # AUTH
    path("signup/", views.Register.as_view(), name="signup"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
