# Estruturas de Dados e Algoritmos

Projeto desenvolvido para a disciplina de **Estruturas de Dados e Algoritmos** do curso de Tecnologia em Ciência de Dados da Universidade Estadual da Paraíba (UEPB).

O projeto implementa diferentes estruturas de dados lineares e não lineares em Python, permitindo que o usuário interaja com cada estrutura por meio de menus no terminal.

O objetivo é demonstrar o funcionamento das principais operações de cada estrutura, reforçando os conceitos estudados durante a disciplina.

---

## Estruturas Implementadas

### Estruturas Lineares

- Pilha (Stack)
- Fila (Queue)
- Lista Encadeada Simples
- Lista Duplamente Encadeada

### Árvores

- Árvore Binária de Busca (BST)
- Árvore AVL
- Árvore B

---

## Funcionalidades

Cada estrutura possui um conjunto de operações para manipulação e consulta dos dados.

### Pilha

- Inserção
- Remoção
- Consulta ao topo
- Exibição dos elementos
- Quantidade de elementos

### Fila

- Inserção
- Remoção
- Consulta ao primeiro elemento
- Consulta ao último elemento
- Exibição dos elementos
- Quantidade de elementos

### Lista Encadeada Simples

- Inserção
- Remoção
- Busca
- Exibição
- Quantidade de elementos

### Lista Duplamente Encadeada

- Inserção
- Remoção
- Exibição direta
- Exibição reversa
- Quantidade de elementos

### Árvore Binária de Busca (BST)

- Inserção
- Remoção
- Busca
- Percurso em ordem
- Percurso em pré-ordem
- Percurso em pós-ordem
- Cálculo da altura
- Quantidade de nós

### Árvore AVL

- Inserção
- Remoção
- Busca
- Percurso em ordem
- Percurso em pré-ordem
- Cálculo da altura
- Quantidade de nós

### Árvore B

- Inserção
- Busca
- Exibição por níveis
- Cálculo da altura
- Quantidade de chaves

---

## Organização do Projeto

```text
Estrutura_de_dados_e_alg/
│
├── linear/
│   ├── __init__.py
│   ├── stack.py
│   ├── queue.py
│   ├── singly_linked_list.py
│   └── doubly_linked_list.py
│
├── trees/
│   ├── __init__.py
│   ├── tree_node.py
│   ├── binary_search_tree.py
│   ├── avl.py
│   └── b_tree.py
│
├── main.py
└── README.md
