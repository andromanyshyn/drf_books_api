from django.contrib import admin
from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'last_name',
        'id', 'date_of_birth',
    )
    fields = (
        'username', 'last_name',
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'description', 'publish_date',
        'author', 'id',
    )