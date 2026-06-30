import unittest
from models.mochila_model import MochilaModel 

class TestProblemaDaMochila(unittest.TestCase):

    def setUp(self):
        self.mochila = MochilaModel()

    def test_caso_padrao(self):
        capacidade = 5.0
        itens = [
            {'peso': 1, 'valor': 5},
            {'peso': 2, 'valor': 4},
            {'peso': 4, 'valor': 8},
            {'peso': 5, 'valor': 6}
        ]
        valor_total, itens_selecionados = self.mochila.resolver_knapsack(capacidade, itens)
        self.assertEqual(valor_total, 13)

    def test_capacidade_zero(self):
        capacidade = 0.0
        itens = [{'peso': 2, 'valor': 10}]
        valor_total, itens_selecionados = self.mochila.resolver_knapsack(capacidade, itens)
        self.assertEqual(valor_total, 0)

if __name__ == '__main__':
    unittest.main()
