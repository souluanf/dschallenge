from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase

User = get_user_model()


class TestApiDrf(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.password = '123'
        cls.user = User.objects.create_user(
            'testeapi',
            'testeapi@testeapi.com',
            cls.password,
        )
        cls.client = APIClient()
        url = reverse('token_obtain_pair')
        data = {
            'username': cls.user.username,
            'password': cls.password
        }
        response = cls.client.post(url, data=data)
        cls.tokens = response.data

    # ---------TESTS----------#

    def test_create_aluno(self):
        url = reverse('api-root:alunos-list')
        data = {
            "nome": "Frederico",
            "sobrenome": "Costa",
            "sexo": "M",
            "cpf": "32165498721",
            "email": "test@test.net",
            "telefone": "11954875270",
            "nascimento": "1994-12-28",
            "rua": "Rua Senador Georgino Avelino",
            "numero": "647",
            "bairro": "Itaquera",
            "cidade": "São Paulo",
            "uf": "SP",
            "cep": "08295370"
        }

        auth = 'Bearer {0}'.format(self.tokens['access'])
        response = self.client.post(url, data, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_list_alunos(self):
        url = reverse('api-root:alunos-list')
        auth = 'Bearer {0}'.format(self.tokens['access'])
        response = self.client.get(url, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_aluno_by_name(self):
        url = reverse('busca-nome', args=['Frederico'])
        auth = 'Bearer {0}'.format(self.tokens['access'])
        response = self.client.get(url, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_aluno_by_cpf(self):
        url = reverse('busca-cpf', args=['32165498721'])
        auth = 'Bearer {0}'.format(self.tokens['access'])
        response = self.client.get(url, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_aluno_by_email(self):
        url = reverse('busca-email', args=['test@test.net'])
        auth = 'Bearer {0}'.format(self.tokens['access'])
        response = self.client.get(url, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
