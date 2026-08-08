"""Implementação da Árvore Binária de Busca (BST)."""

from typing import Generic, TypeVar

from .tree_node import TreeNode


T = TypeVar("T")


class BinarySearchTree(Generic[T]):
    """Árvore Binária de Busca."""

    def __init__(self):
        """Inicializa uma árvore vazia."""
        self.root = None


    # =========================
    # Métodos básicos
    # =========================

    def get_root(self):
        """Retorna a raiz da árvore."""
        return self.root


    def is_empty(self) -> bool:
        """Verifica se a árvore está vazia."""
        return self.root is None



    # =========================
    # Inserção
    # =========================

    def insert(self, value: T):
        """Insere um valor na árvore."""
        self.root = self._insert(self.root, value)


    def _insert(self, node, value: T):

        if node is None:
            return TreeNode(value)


        if value < node.data:
            node.left = self._insert(node.left, value)


        elif value > node.data:
            node.right = self._insert(node.right, value)


        return node



    # =========================
    # Busca
    # =========================

    def search(self, value: T):
        """Busca um valor na árvore."""
        return self._search(self.root, value)


    def _search(self, node, value: T):

        if node is None:
            return None


        if value == node.data:
            return node


        if value < node.data:
            return self._search(node.left, value)


        return self._search(node.right, value)



    # =========================
    # Percursos
    # =========================

    def pre_order(self):
        """Percurso raiz -> esquerda -> direita."""
        result = []

        self._pre_order(self.root, result)

        return result


    def _pre_order(self, node, result):

        if node is None:
            return


        result.append(node.data)

        self._pre_order(node.left, result)

        self._pre_order(node.right, result)



    def in_order(self):
        """Percurso esquerda -> raiz -> direita."""
        result = []

        self._in_order(self.root, result)

        return result


    def _in_order(self, node, result):

        if node is None:
            return


        self._in_order(node.left, result)

        result.append(node.data)

        self._in_order(node.right, result)



    def post_order(self):
        """Percurso esquerda -> direita -> raiz."""
        result = []

        self._post_order(self.root, result)

        return result


    def _post_order(self, node, result):

        if node is None:
            return


        self._post_order(node.left, result)

        self._post_order(node.right, result)

        result.append(node.data)



    # =========================
    # Altura
    # =========================

    def height(self):
        """Retorna a altura da árvore."""
        return self._height(self.root)


    def _height(self, node):

        if node is None:
            return -1


        left_height = self._height(node.left)

        right_height = self._height(node.right)


        return 1 + max(left_height, right_height)



    # =========================
    # Quantidade de nós
    # =========================

    def size(self):
        """Retorna a quantidade de nós."""
        return self._size(self.root)


    def _size(self, node):

        if node is None:
            return 0


        return (
            1
            + self._size(node.left)
            + self._size(node.right)
        )



    # =========================
    # Menor elemento
    # =========================

    def _minimum(self, node):

        while node.left is not None:
            node = node.left


        return node



    # =========================
    # Remoção
    # =========================

    def remove(self, value: T):
        """Remove um valor da árvore."""
        self.root = self._remove(self.root, value)



    def _remove(self, node, value: T):

        if node is None:
            return None


        if value < node.data:

            node.left = self._remove(node.left, value)


        elif value > node.data:

            node.right = self._remove(node.right, value)


        else:

            # Caso 1: nó folha
            if node.left is None and node.right is None:
                return None


            # Caso 2: somente filho direito
            if node.left is None:
                return node.right


            # Caso 3: somente filho esquerdo
            if node.right is None:
                return node.left


            # Caso 4: dois filhos
            successor = self._minimum(node.right)

            node.data = successor.data

            node.right = self._remove(
                node.right,
                successor.data
            )


        return node