from rest_framework import permissions

from api.models import Shop


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `creator` attribute.
    """

    def has_object_permission(self, request, view, obj):
        """This method contains check if the obj is Shop instance, otherwise, when checking the shop creator,
        the creator attr will be accessed throw additional attr shop """

        if request.method in permissions.SAFE_METHODS:
            return True
        if isinstance(obj, Shop):
            return obj.creator == request.user
        else:
            return obj.shop.creator == request.user


class IsOwnerOfShopOrReadOnly(permissions.BasePermission):
    """
    Permission to only allow owners of shop object to add books to it.
    Assumes the model instance has an `creator` attribute.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        shop_obj = Shop.objects.get(pk=view.kwargs.get('pk'))
        return shop_obj.creator == request.user
