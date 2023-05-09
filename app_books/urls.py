from django.urls import path
from . import views

urlpatterns = [
    path('book/list', views.BookAPIList.as_view(), name='book_list'),
    path('book/<int:book_id>', views.BookAPIRetrieve.as_view(), name='book'),
    path('book/create/', views.BookAPICreate.as_view(), name='book_create'),
    path('book/update/<int:book_id>/', views.BookAPIUpdate.as_view(), name='book_update'),
    path('book/delete/<int:book_id>/', views.BookAPIDelete.as_view(), name='book_delete'),
]
