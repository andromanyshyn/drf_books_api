from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .models import Book
from .serializers import BookSerializer


class BookAPIList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BookAPIRetrieve(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data)


class BookAPICreate(CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        if request.user.pk != int(request.data['author']):
            return Response('User should be author of the book', status=HTTP_400_BAD_REQUEST)
        else:
            return super().create(request)


class BookAPIUpdate(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def put(self, request, book_id):
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class BookAPIDelete(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def delete(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
        except Exception:
            return Response(HTTP_400_BAD_REQUEST)
        book.delete()
        return Response(HTTP_204_NO_CONTENT)
