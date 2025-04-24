# 🧠 Estrutura de Dados – Listas Encadeadas e Ordenadas em Python

![Gojo Satoru](https://media.giphy.com/media/zeXv4Sxy72RUA/giphy.gif)

Este projeto é parte das atividades da disciplina de **Estrutura de Dados**, com foco na implementação de **listas encadeadas** (simples) e **listas ordenadas** em Python, utilizando conceitos básicos de ponteiros e manipulação de nós.

---

## 📁 Estrutura do Projeto

```
estrutura-de-dados/
├── node.py                  ← Classe Node (nó)
├── Lista_simples.py         ← Lista encadeada com inserção, busca e exclusão
├── Lista_ordenada.py        ← Inserção ordenada
├── teste_listas.py          ← Script de testes para as listas
└── README.md                ← Este arquivo
```

---

## 🧩 Conteúdo

### 🔹 `Node`
Arquivo: `node.py`  
Classe que representa um nó da lista, com atributos `valor` e `proximo`.

### 🔹 Lista Encadeada Simples
Arquivo: `Lista_simples.py`  
Implementa os métodos:
- `inserir(valor)` – Insere no início da lista.
- `buscar(valor)` – Verifica se o valor está presente na lista.
- `excluir(valor)` – Remove um valor, se existir.
- `__str__()` – Retorna os elementos da lista em formato legível.

### 🔹 Lista Ordenada
Arquivo: `Lista_ordenada.py`  
Implementa a inserção mantendo os elementos em ordem crescente com:
- `inserir_ordenado(valor)`
- `__str__()` – Representação visual da lista ordenada.

---

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/estrutura-de-dados.git
   cd estrutura-de-dados
   ```

2. Execute o arquivo de testes:
   ```bash
   python teste_listas.py
   ```

---

## 💡 Exemplo de Saída Esperada

```
=== Lista Simples ===
Lista após inserções: 20 -> 5 -> 10
Busca 10: True
Busca 30: False
Lista após excluir 5: 20 -> 10
Valor 99 não encontrado.

=== Lista Ordenada ===
Lista ordenada: 5 -> 10 -> 15 -> 20
```

---

## 📌 Requisitos

- Python 3.8 ou superior
- Nenhuma biblioteca externa necessária

---

## 👩‍🏫 Informações Acadêmicas

- **Disciplina:** Estrutura de Dados
- **Professor(a):** Kadidja
- **Semestre:** 3º semestre de 2025
