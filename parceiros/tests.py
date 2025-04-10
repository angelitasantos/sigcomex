from django.test import TestCase
from parceiros.models import Teste1Categoria, Teste1Grupo, Teste1Cliente


class Teste1ModelsTest(TestCase):

    def test_debug(self):
        print("Rodando teste básico...")
        self.assertTrue(True)

    def setUp(self):
        self.categoria = Teste1Categoria.objects.create(
            nome="Categoria Teste", status="A"
        )
        self.grupo = Teste1Grupo.objects.create(
            nome="Grupo Teste", status="I"
        )

    def test_criacao_categoria(self):
        self.assertEqual(self.categoria.nome, "Categoria Teste")
        self.assertEqual(self.categoria.status, "A")
        self.assertEqual(str(self.categoria), "Categoria Teste")

    def test_criacao_grupo(self):
        self.assertEqual(self.grupo.nome, "Grupo Teste")
        self.assertEqual(self.grupo.status, "I")
        self.assertEqual(str(self.grupo), "Grupo Teste")

    def test_criacao_cliente(self):
        cliente = Teste1Cliente.objects.create(
            nome="Cliente 1",
            razao_social="Cliente Razão Social",
            cnpj="00.000.000/0001-00",
            insc_est="123456",
            sigla_imp="IMP",
            sigla_exp="EXP",
            serv_sigla_imp="SIMP",
            serv_sigla_exp="SEXP",
            cod_interno="INT001",
            observacoes="Cliente teste de observações.",
            status="A",
            grupo=self.grupo,
            categoria=self.categoria
        )

        self.assertEqual(cliente.nome, "Cliente 1")
        self.assertEqual(cliente.status, "A")
        self.assertEqual(cliente.grupo.nome, "Grupo Teste")
        self.assertEqual(cliente.categoria.nome, "Categoria Teste")
        self.assertEqual(str(cliente), "Cliente 1")

    def test_cliente_campos_opcionais(self):
        cliente = Teste1Cliente.objects.create(
            nome="Cliente Sem Dados",
            status="I"
        )
        self.assertIsNone(cliente.razao_social)
        self.assertIsNone(cliente.cnpj)
        self.assertEqual(cliente.status, "I")
        self.assertEqual(str(cliente), "Cliente Sem Dados")
