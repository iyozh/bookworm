from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Shop(models.Model):
    """Implementation of Shop Model.
    Fields: name"""

    name = models.CharField(max_length=255, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
