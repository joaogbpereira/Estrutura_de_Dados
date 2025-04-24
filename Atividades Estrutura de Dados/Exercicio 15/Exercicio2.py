# 2. Simular uma fila de prioridade para tarefas da expedição espacial

import heapq

# Lista de tarefas com prioridade (quanto menor o número, maior a prioridade)
# Cada tupla tem (prioridade, descrição)
tarefas = [
    (3, "Recolher amostras"),
    (1, "Consertar nave"),
    (2, "Estabelecer comunicação com base"),
    (4, "Explorar nova caverna")
]

# Transformar a lista numa fila de prioridade (min-heap)
heapq.heapify(tarefas)

# Simulando execução das tarefas por ordem de prioridade
print("Execução das tarefas em ordem de prioridade:")
while tarefas:
    prioridade, tarefa = heapq.heappop(tarefas)
    print(f"- {tarefa} (prioridade {prioridade})")
