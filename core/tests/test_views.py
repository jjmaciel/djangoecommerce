# coding=utf-8

from django.test import TestCase, Client   # o client é o simulador do navegador
from django.urls import reverse    # usada para substituir a chamada manual da url

class IndexViewTestCase(TestCase):

    # esta função é sempre chamada quando se executa o teste
    # se quiser criar alguma coisa, cria-se aqui. Ex: uma váriavel para ser usada em outras funções
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    # esta função é executada no final do teste
    # se tem alguma coisa a ser deletada no final do teste, coloca-se aqui
    def tearDown(self):
        pass

    def test_status_code(self):
        response = self.client.get(self.url)  # o get é o metodo get do http
        # o TestCase tem vários assert, entre eles o assertEquals
        # o 200 é a resposta se o site está ok, diferente do 404 que é quando não encontra
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        # testa se está usando o template index.html
        self.assertTemplateUsed(response, 'index.html')


"""
nas versões mais antigas do Django o reverse era diferente
from django.core.urlresolvers import reverse
"""