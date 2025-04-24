from node import Node

class ListaSimples:
    def __init__(self):
        self.inicio = None

    def inserir(self, valor):
        novo = Node(valor)
        novo.proximo = self.inicio
        self.inicio = novo

    def excluir(self, valor):
        atual = self.inicio
        anterior = None

        while atual is not None and atual.valor != valor:
            anterior = atual
            atual = atual.proximo

        if atual is None:
            print(f"Valor {valor} não encontrado.")
            return

        if anterior is None:
            self.inicio = atual.proximo
        else:
            anterior.proximo = atual.proximo

    def buscar(self, valor):
        atual = self.inicio
        while atual is not None:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False

    def __str__(self):
        elementos = []
        atual = self.inicio
        while atual is not None:
            elementos.append(str(atual.valor))
            atual = atual.proximo
        return " -> ".join(elementos)
