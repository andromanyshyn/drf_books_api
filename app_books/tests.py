import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books_authors_project.settings')
import django

django.setup()
from .models import *
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from django.urls import reverse


class APIBookTestCase(APITestCase):

    def setUp(self):
        self.user = Author.objects.create_user(username='testusername',
                                               password='testpassword')

        self.book1 = Book.objects.create(title='test_title1',
                                        description='test_description1',
                                        author=self.user)
        self.book2 = Book.objects.create(title='test_title2',
                                         description='test_description2',
                                         author=self.user)
        self.book3 = Book.objects.create(title='test_title3',
                                         description='test_description3',
                                         author=self.user)

        self.token = Token.objects.create(user=self.user)

        self.url_list = reverse('book_list')

    def test_list_books(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(self.url_list)

        self.assertEqual(len(response.data), Book.objects.all().count())
        self.assertEqual(response.data[0]['title'], Book.objects.first().title)
        self.assertEqual(response.data[1]['author'], Book.objects.get(id=2).author.id)
