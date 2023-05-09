from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date


class Author(AbstractUser):
    first_name = None
    date_of_birth = models.DateField(default=date.today)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Author'


class Book(models.Model):
    title = models.CharField(max_length=32, unique=True)
    description = models.TextField()
    publish_date = models.DateField(default=date.today)
    author = models.ForeignKey(
        to=Author, on_delete=models.CASCADE,
        related_name='books', default=''
    )

    class Meta:
        ordering = (
            'title',
        )
