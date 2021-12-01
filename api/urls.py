from django.urls import path

from api import views

urlpatterns = [
    path("shops/", views.ShopListView.as_view()),
    path("shops/<int:pk>", views.ShopRetrieveUpdateDestroyView.as_view()),
]
