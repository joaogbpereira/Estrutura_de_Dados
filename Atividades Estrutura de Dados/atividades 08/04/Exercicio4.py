# 4. Sistema de Impressão de Documentos

class Documento:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None

class FilaImpressao:
    def __init__(self):
        self.head = None
        self.tail = None

    def adicionar_documento(self, nome):
        novo_documento = Documento(nome)
        if not self.head:
            self.head = novo_documento
            self.tail = novo_documento
        else:
            self.tail.proximo = novo_documento
            self.tail = novo_documento
        print(f"Documento '{nome}' adicionado à fila.")

    def imprimir_documento(self):
        if self.head:
            documento_impresso = self.head.nome
            self.head = self.head.proximo
            if not self.head:
                self.tail = None
            print(f"Imprimindo documento: {documento_impresso}")
            return documento_impresso
        else:
            print("A fila de impressão está vazia.")
            return None

    def mostrar_fila(self):
        atual = self.head
        if not atual:
            print("A fila de impressão está vazia.")
            return
        print("Fila de impressão:")
        while atual:
            print(f"- {atual.nome}")
            atual = atual.proximo

# Exemplo de uso
fila = FilaImpressao()
fila.adicionar_documento("Relatório Financeiro")
fila.adicionar_documento("Apresentação de Vendas")
fila.adicionar_documento("Contrato")
fila.mostrar_fila()
fila.imprimir_documento()
fila.mostrar_fila()
fila.imprimir_documento()
fila.imprimir_documento()
fila.imprimir_documento()
