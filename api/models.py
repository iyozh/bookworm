from django.db import models


class Shop(models.Model):
    """Implementation of Shop Model.
    Fields: name"""

    name = models.CharField(max_length=255, unique=True)

