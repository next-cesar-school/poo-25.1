import unittest
from tarefas import SistemaGerenciamentoTarefas
#from aula11.praticas.tarefas import SistemaGerenciamentoTarefas

class TestSistemaGerenciamentoTarefas(unittest.TestCase):
    def test_id_adicionar_tarefas(self):
        tarefas = SistemaGerenciamentoTarefas()
        id_tar1 = tarefas.adicionar_tarefa("Fazer a feira")
        id_tar2 = tarefas.adicionar_tarefa("Lavar os pratos")
        id_tar3 = tarefas.adicionar_tarefa("Mudar para o tema escuro do VS Code")

        self.assertEqual(id_tar1, 1)
        self.assertEqual(id_tar2, 2)
        self.assertEqual(id_tar3, 3)

    def test_listar_tarefas(self):
        tarefas = SistemaGerenciamentoTarefas()
        descricao_original = 'Fazer a feira'
        id_tar1 = tarefas.adicionar_tarefa(descricao_original)
        lista_tarefas = tarefas.listar_tarefas()

        self.assertEqual(lista_tarefas[0]['id'], id_tar1)
        self.assertEqual(lista_tarefas[0]['descricao'], descricao_original)
        self.assertFalse(lista_tarefas[0]['concluida'])

if __name__ == '__main__':
    unittest.main()
