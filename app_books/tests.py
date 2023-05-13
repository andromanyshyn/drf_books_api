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
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        """endpoints"""
        self.url_list = reverse('book_list')
        self.url_get_book = reverse('book', kwargs={'book_id': self.book1.id})
        self.url_create_book = reverse('book_create')
        self.url_update_book = reverse('book_update', kwargs={'book_id': self.book1.id})
        self.url_delete_book = reverse('book_delete', kwargs={'book_id': self.book1.id})

    def test_books_list_view(self):
        response = self.client.get(self.url_list)

        self.assertEqual(len(response.data), Book.objects.all().count())
        self.assertEqual(response.data[0]['title'], Book.objects.first().title)
        self.assertEqual(response.data[1]['author'], Book.objects.get(id=2).author.id)

    def test_book_detail_view(self):
        response = self.client.get(self.url_get_book)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], Book.objects.first().id)
        self.assertEqual(response.data['author'], Book.objects.first().author.id)

    def test_book_create(self):
        data_create = {
            "id": 5,
            "title": "test_title4",
            "description": "test_description4",
            "author": self.user.id
        }

        self.assertFalse(Book.objects.filter(title="test_title4").exists())
        response = self.client.post(self.url_create_book, data=data_create)

        self.assertEqual(response.status_code, 201)
        self.assertTrue(Book.objects.filter(title="test_title4").exists())
        self.assertEqual(Book.objects.last().title, data_create['title'])

    def test_book_update(self):
        data_update = {
            "id": self.book1.id,
            "title": "update_test_title1",
            "description": "update_test_description1",
            "author": self.user.id
        }

        self.assertFalse(Book.objects.filter(title='update_test_title1').exists())
        response = self.client.put(self.url_update_book, data=data_update)

        self.assertEqual(response.status_code, 201)
        print(Book.objects.all())
        self.assertTrue(Book.objects.filter(title='update_test_title1').exists())

    def test_book_delete(self):
        response = self.client.delete(self.url_delete_book)

        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())
