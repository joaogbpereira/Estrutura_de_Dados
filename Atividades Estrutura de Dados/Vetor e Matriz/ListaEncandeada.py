class Tarefa:
    def __init__(self, nome):
        self.nome = nome
        self.proxima = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def adicione_tarefa(self, nome):
        nova_tarefa = Tarefa(nome)
        nova_tarefa.proxima = self.head
        self.head = nova_tarefa

    def remove_tarefa(self, nome):
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