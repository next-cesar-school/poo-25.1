"""
Módulo para a classe SistemaGerenciamentoTarefas.
Este módulo define um sistema simples para adicionar, listar,
marcar como concluída e remover tarefas.
"""

class SistemaGerenciamentoTarefas:
    """
    Gerencia uma coleção de tarefas, permitindo adição, listagem,
    atualização de status e remoção.

    Atributos:
        _tarefas (dict): Um dicionário onde as chaves são IDs de tarefas
                         (inteiros) e os valores são dicionários representando
                         cada tarefa (e.g., {'descricao': 'Estudar Python', 'concluida': False}).
        _proximo_id (int): O próximo ID disponível para uma nova tarefa,
                           garantindo unicidade.
    """

    def __init__(self):
        """
        Inicializa o sistema de gerenciamento de tarefas com uma lista vazia.
        """
        self._tarefas = {}
        self._proximo_id = 1

    def adicionar_tarefa(self, descricao: str) -> int:
        """
        Adiciona uma nova tarefa ao sistema.

        Args:
            descricao (str): A descrição da tarefa a ser adicionada.

        Returns:
            int: O ID único da tarefa recém-adicionada.

        Raises:
            ValueError: Se a descrição da tarefa for vazia ou não for uma string.
        """
        if not isinstance(descricao, str) or not descricao.strip():
            raise ValueError("A descrição da tarefa não pode ser vazia.")

        tarefa = {
            'descricao': descricao.strip(),
            'concluida': False
        }
        self._tarefas[self._proximo_id] = tarefa
        self._proximo_id += 1
        return self._proximo_id - 1 # Retorna o ID da tarefa que acabou de ser adicionada

    def listar_tarefas(self) -> list:
        """
        Lista todas as tarefas atualmente no sistema.

        Returns:
            list: Uma lista de dicionários, onde cada dicionário representa uma tarefa
                  e inclui seu 'id', 'descricao' e 'concluida'.
        """
        lista_completa = []
        for id_tarefa, detalhes in self._tarefas.items():
            lista_completa.append({
                'id': id_tarefa,
                'descricao': detalhes['descricao'],
                'concluida': detalhes['concluida']
            })
        return lista_completa

    def concluir_tarefa(self, id_tarefa: int) -> bool:
        """
        Marca uma tarefa específica como concluída.

        Args:
            id_tarefa (int): O ID da tarefa a ser marcada como concluída.

        Returns:
            bool: True se a tarefa foi marcada como concluída, False se já estava concluída.

        Raises:
            ValueError: Se o ID da tarefa não for encontrado.
        """
        if id_tarefa not in self._tarefas:
            raise ValueError(f"Tarefa com ID {id_tarefa} não encontrada.")

        if self._tarefas[id_tarefa]['concluida']:
            return False # Já estava concluída

        self._tarefas[id_tarefa]['concluida'] = True
        return True

    def remover_tarefa(self, id_tarefa: int) -> None:
        """
        Remove uma tarefa do sistema.

        Args:
            id_tarefa (int): O ID da tarefa a ser removida.

        Raises:
            ValueError: Se o ID da tarefa não for encontrado.
        """
        if id_tarefa not in self._tarefas:
            raise ValueError(f"Tarefa com ID {id_tarefa} não encontrada.")
        del self._tarefas[id_tarefa]

if __name__ == '__main__':
    ...
