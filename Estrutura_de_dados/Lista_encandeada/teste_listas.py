from Lista_simples import ListaSimples
from Lista_ordenada import ListaOrdenada

# Testando Lista Simples
print("=== Lista Simples ===")
lista_simples = ListaSimples()
lista_simples.inserir(10)
lista_simples.inserir(5)
lista_simples.inserir(20)

print("Lista após inserções:", lista_simples)
print("Busca 10:", lista_simples.buscar(10))
print("Busca 30:", lista_simples.buscar(30))

lista_simples.excluir(5)
print("Lista após excluir 5:", lista_simples)

lista_simples.excluir(99)  # Valor inexistente

# Testando Lista Ordenada
print("\n=== Lista Ordenada ===")
lista_ordenada = ListaOrdenada()
lista_ordenada.inserir_ordenado(10)
lista_ordenada.inserir_ordenado(5)
lista_ordenada.inserir_ordenado(20)
lista_ordenada.inserir_ordenado(15)

print("Lista ordenada:", lista_ordenada)
