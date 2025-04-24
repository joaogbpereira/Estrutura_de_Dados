# 🧠 Atividade 25/03 (Não Presencial) – *O Jogo da Imitação* e Estruturas de Dados

Esta atividade explora conceitos de estruturas de dados a partir do contexto do filme *O Jogo da Imitação*...

A proposta é analisar como **filas**, **pilhas** e **listas** podem ser aplicadas em situações similares àquelas enfrentadas no desenvolvimento da máquina, relacionando teoria e prática de forma criativa.

---

## 🔁 1. Fila no Processamento de Combinações

**Resposta:**  
Uma **fila** organiza as combinações do Enigma na ordem em que são geradas, seguindo a lógica **FIFO** (*First In, First Out*). Isso significa que:

- Cada tentativa de combinação é enfileirada conforme é gerada.
- As tentativas são processadas sequencialmente, garantindo que:
  - Nenhuma combinação seja ignorada.
  - O sistema teste todas as possibilidades, sem repetições.

**Exemplo:**  
Se a fila contém: `AAA`, `AAB`, `AAC`, a máquina testará na ordem:
1. AAA  
2. AAB  
3. AAC  

---

## 🧱 2. Pilha para Reverter Decisões

**Resposta:**  
Uma **pilha** é usada para retroceder em decisões anteriores quando uma tentativa falha, seguindo a lógica **LIFO** (*Last In, First Out*).

### Funcionamento:
1. **Empilhar:**  
   Cada configuração testada (como o estado atual dos rotores) é salva no topo da pilha.
2. **Desempilhar:**  
   Caso a combinação falhe:
   - O estado atual é removido da pilha.
   - A máquina retorna automaticamente ao estado anterior (agora no topo).

**Vantagem:**  
Evita o reinício do processo desde o começo, economizando tempo e recursos computacionais.

---

## 📚 3. Lista de Padrões Testados

**Resposta:**  
Uma **lista** é usada para armazenar todas as combinações ou padrões já testados, a fim de evitar tentativas duplicadas.

### Comparação: Lista Encadeada vs Vetor

| Critério            | Lista Encadeada                         | Vetor                                |
|---------------------|------------------------------------------|--------------------------------------|
| Crescimento         | Dinâmico (sem tamanho fixo)              | Estático ou com redimensionamento    |
| Inserção/Remoção    | Rápida (sem realocação)                  | Mais lenta (possível realocação)     |
| Eficiência Geral    | Melhor para armazenar dados variáveis    | Menos eficiente para esse contexto   |

**Conclusão:**  
A **lista encadeada** é mais eficiente nesse cenário pois:
- Cresce conforme necessário.
- Permite inserções e remoções com menor custo computacional.

---

## ✅ Conclusão

Esses três conceitos — **fila**, **pilha** e **lista** — são fundamentais para resolver problemas complexos de forma organizada e eficiente, como visto no contexto histórico retratado por *O Jogo da Imitação*. Aplicar essas estruturas de dados permite criar algoritmos mais robustos, reutilizáveis e lógicos.

---

Aluno -> JOÃO GABRIEL PEREIRA DE ARAUJO
Curso -> Engenharia de Software
