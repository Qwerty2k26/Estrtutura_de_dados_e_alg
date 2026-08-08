 # Estruturas de Dados e Algoritmos

## Descrição

Este projeto foi desenvolvido para a disciplina de **Estruturas de Dados e Algoritmos** do curso de Tecnologia em Ciência de Dados da Universidade Estadual da Paraíba (UEPB).

O sistema implementa estruturas de dados lineares e não lineares em Python, permitindo que o usuário interaja com cada estrutura através de menus no terminal.

O objetivo do projeto é demonstrar o funcionamento das principais operações de cada estrutura, reforçando os conceitos estudados durante a disciplina.

---

# Estruturas implementadas

## Estruturas Lineares

- Pilha (Stack)
- Fila (Queue)
- Lista Encadeada Simples
- Lista Duplamente Encadeada

## Árvores

- Árvore Binária de Busca (BST)
- Árvore AVL
- Árvore B

---

# Funcionalidades

Cada estrutura possui um menu próprio contendo suas operações.

Entre elas:

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

### Árvore BST

- Inserção
- Remoção
- Busca
- Percurso em ordem
- Percurso em pré-ordem
- Percurso em pós-ordem
- Altura
- Quantidade de nós

### Árvore AVL

- Inserção
- Remoção
- Busca
- Percurso em ordem
- Percurso em pré-ordem
- Altura
- Quantidade de nós

### Árvore B

- Inserção
- Busca
- Exibição por níveis
- Altura
- Quantidade de chaves

---

# Organização do Projeto

```
EDA/
│
├── linear/
│   ├── stack.py
│   ├── queue.py
│   ├── singly_linked_list.py
│   ├── doubly_linked_list.py
│
├── trees/
│   ├── tree_node.py
│   ├── binary_search_tree.py
│   ├── avl.py
│   ├── b_tree.py
│
├── main.py
└── README.md
```

---

# Tecnologias Utilizadas

- Python 3.12
- Visual Studio Code

---

# Como executar

Clone o projeto:

```bash
git clone <url-do-repositório>
```

Entre na pasta:

```bash
cd EDA
```

Execute:

```bash
python main.py
```

---

# Conceitos aplicados

Durante o desenvolvimento foram utilizados conceitos como:

- Programação Orientada a Objetos
- Classes
- Objetos
- Encapsulamento
- Recursão
- Generics (TypeVar e Generic)
- Estruturas Lineares
- Estruturas Hierárquicas
- Árvores Balanceadas
- Organização modular do código

---

# Melhorias Futuras

Como evolução do projeto, pretende-se implementar:

- tratamento de exceções para entradas inválidas;
- limpeza automática da tela durante a navegação;
- persistência de dados em arquivos;
- interface gráfica;
- testes automatizados;
- remoção de chaves na Árvore B;
- documentação utilizando Sphinx.

---

# Autor

**Chrystian**

Curso de Tecnologia em Ciência de Dados

Universidade Estadual da Paraíba - UEPB
