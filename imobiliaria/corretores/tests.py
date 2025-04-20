from django.test import TestCase
from .models import Corretor

class CorretorModelTest(TestCase):
    def setUp(self):
        self.corretor = Corretor.objects.create(
            nome="João Silva",
            email="joao@example.com",
            telefone="+5511999999999",
            creci="123456"
        )

    def test_criacao_corretor(self):
        self.assertEqual(self.corretor.nome, "João Silva")
        self.assertEqual(self.corretor.email, "joao@example.com")
        self.assertEqual(self.corretor.telefone, "+5511999999999")
        self.assertEqual(self.corretor.creci, "123456")

    def test_listar_corretores_view(self):
        response = self.client.get('/corretores/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "João Silva")
