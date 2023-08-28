from django.contrib.auth.models import AbstractUser
from django.db import models


class Author(AbstractUser):
    date_of_birth = models.DateField()

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Author'


class Book(models.Model):
    title = models.CharField(max_length=32, unique=True)
    description = models.TextField()
    publish_date = models.DateField()
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
