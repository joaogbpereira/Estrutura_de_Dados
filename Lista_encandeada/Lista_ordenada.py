from node import Node

class ListaOrdenada:
    def __init__(self):
        self.inicio = None

    def inserir_ordenado(self, valor):
        novo = Node(valor)

        if self.inicio is None or valor < self.inicio.valor:
            novo.proximo = self.inicio
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.proximo is not None and atual.proximo.valor < valor:
                atual = atual.proximo

            novo.proximo = atual.proximo
            atual.proximo = novo

    def __str__(self):
        elementos = []
        atual = self.inicio
        while atual is not None:
            elementos.append(str(atual.valor))
            atual = atual.proximo
        return " -> ".join(elementos)
