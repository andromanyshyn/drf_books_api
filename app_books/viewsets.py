from app_books.models import Book
from app_books.serializers import BookSerializer
from rest_framework import viewsets
from app_books.permissions import CanInteractWithBookAPI


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [CanInteractWithBookAPI]
