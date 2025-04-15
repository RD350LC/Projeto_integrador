from django.test import TestCase
from django.urls import reverse

class FrontendTests(TestCase):
    def test_pagina_inicial_status_code(self):
        response = self.client.get(reverse('pagina_inicial'))
        self.assertEqual(response.status_code, 200)
