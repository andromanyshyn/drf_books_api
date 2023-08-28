from rest_framework import serializers
from app_books.models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = "__all__"

