from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Shop(models.Model):
    """Implementation of Shop Model.
    Fields: name, creator"""

    name = models.CharField(max_length=255, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


class Book(models.Model):
    """Implementation of Book Model
    Fields: title, author, description, published, pages, genre, cover_type, amount_limit, time_limit, shop"""

    class Genres(models.TextChoices):
        FICTION = "Fiction"
        NON_FICTION = "Non-fiction"
        DETECTIVE = "Detective"
        HORROR = "Horror"
        COMEDY = "Comedy"

    class CoverTypes(models.TextChoices):
        HARD = "Hard"
        SOFT = "Soft"

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    published = models.DateField()
    pages = models.IntegerField()
    genre = models.CharField(
        max_length=255,
        choices=Genres.choices,
        default=Genres.NON_FICTION,
    )
    cover_type = models.CharField(
        max_length=100,
        choices=CoverTypes.choices,
        default=CoverTypes.HARD,
    )
    amount_limit = models.IntegerField()
    time_limit = models.DateTimeField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
