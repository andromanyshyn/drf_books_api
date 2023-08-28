from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app_books.viewsets import BookViewset

router = DefaultRouter()
router.register("", BookViewset, basename="book")
urlpatterns = [
    path("book/", include(router.urls))
]
