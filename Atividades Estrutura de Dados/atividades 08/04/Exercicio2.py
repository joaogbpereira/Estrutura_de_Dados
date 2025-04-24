# 2. Agenda Telefônica com Lista Duplamente Encadeada

class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.anterior = None
        self.proximo = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.head = None

    def adicionar_contato(self, nome, telefone):
        novo_contato = Contato(nome, telefone)
        novo_contato.proximo = self.head
        if self.head:
            self.head.anterior = novo_contato
        self.head = novo_contato

    def remover_contato(self, nome):
        atual = self.head
        while atual and atual.nome != nome:
            atual = atual.proximo
        if atual:
            if atual.anterior:
                atual.anterior.proximo = atual.proximo
            if atual.proximo:
                atual.proximo.anterior = atual.anterior
            if atual == self.head:
                self.head = atual.proximo

    def buscar_contato(self, nome):
        atual = self.head
        while atual:
            if atual.nome == nome:
                return f"Contato encontrado: {atual.nome} - {atual.telefone}"
            atual = atual.proximo
        return "Contato não encontrado"

# Exemplo de uso
agenda = ListaDuplamenteEncadeada()
agenda.adicionar_contato("Alice", "123456789")
agenda.adicionar_contato("Bob", "987654321")
print(agenda.buscar_contato("Bob"))
agenda.remover_contato("Alice")
print(agenda.buscar_contato("Alice"))
