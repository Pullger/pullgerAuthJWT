from rest_framework.test import APITestCase
from . import UnitOperations


class Test_001_Token(APITestCase):
    def setUp(self):
        UnitOperations.CreateUser(self)

    def Test_GetToken(self):
        UnitOperations.GetToken(self)