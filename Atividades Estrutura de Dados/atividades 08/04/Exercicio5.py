# 5. Autocomplete em Buscas

class Node:
    def __init__(self, data):
        self.data = data
        self.proximo = None

class ListaEncadeadaAutocomplete:
    def __init__(self):
        self.head = None

    def adicionar_palavra(self, palavra):
        novo_node = Node(palavra)
        if not self.head:
            self.head = novo_node
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_node

    def sugerir_palavras(self, prefixo):
        sugestoes = []
        atual = self.head
        while atual:
            if atual.data.startswith(prefixo):
                sugestoes.append(atual.data)
            atual = atual.proximo
        return sugestoes

# Exemplo de uso
autocomplete = ListaEncadeadaAutocomplete()
autocomplete.adicionar_palavra("apple")
autocomplete.adicionar_palavra("apricot")
autocomplete.adicionar_palavra("banana")
autocomplete.adicionar_palavra("grape")
autocomplete.adicionar_palavra("application")

print(f"Sugestões para 'ap': {autocomplete.sugerir_palavras('ap')}")
print(f"Sugestões para 'ba': {autocomplete.sugerir_palavras('ba')}")
print(f"Sugestões para 'g': {autocomplete.sugerir_palavras('g')}")
print(f"Sugestões para 'or': {autocomplete.sugerir_palavras('or')}")
