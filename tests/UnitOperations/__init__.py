from django.contrib.auth.models import User
from rest_framework.test import APITestCase

def CreateUser(self: APITestCase):
    self.username = "test";
    self.password = "qwerty";
    User.objects.create_user(username=self.username, password=self.password)

def GetToken(self: APITestCase):
    tokenRequest = self.client.post('/api/account/login/', {"username": self.username, "password": self.password})
    self.assertEqual(tokenRequest.status_code, 200, 'Incorrest login status')

    token = tokenRequest.data.get('token')
    self.assertIsNotNone(token, 'Incorrect token return.')
    self.assertEqual(len(token), 40, 'Incorrect token')

    self.token = token