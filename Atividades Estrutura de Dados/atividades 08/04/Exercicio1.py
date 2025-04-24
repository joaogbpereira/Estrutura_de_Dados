# 1 Implementação de Lista Encadeada para Gerenciamento de Tarefas

class Tarefa:
    def __init__(self, nome):
        self.nome = nome
        self.proxima = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def adicionar_tarefa(self, nome):
        nova_tarefa = Tarefa(nome)
        nova_tarefa.proxima = self.head
        self.head = nova_tarefa

    def remover_tarefa(self, nome):
        atual = self.head
        anterior = None
        while atual and atual.nome != nome:
            anterior = atual
            atual = atual.proxima
        if atual:
            if anterior:
                anterior.proxima = atual.proxima
            else:
                self.head = atual.proxima

    def mostrar_tarefas(self):
        atual = self.head
        while atual:
            print(atual.nome)
            atual = atual.proxima

# Exemplo de uso
lista_tarefas = ListaEncadeada()
lista_tarefas.adicionar_tarefa("Estudar Estruturas de Dados")
lista_tarefas.adicionar_tarefa("Revisar Código")
print("Tarefas iniciais:")
lista_tarefas.mostrar_tarefas()
lista_tarefas.remover_tarefa("Revisar Código")
print("\nTarefas após remover 'Revisar Código':")
lista_tarefas.mostrar_tarefas()
