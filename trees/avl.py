""""Criando a árvore de bsca binária com balanceamento"""
#Importando o nó a biblioteca typing e a BST para usar como herança
from typing import TypeVar

from .tree_node import TreeNode
from .binary_search_tree import BinarySearchTree

T = TypeVar("T")


class AVLNode(TreeNode[T]):
    def __init__(self, data: T):
        super().__init__(data)
        self.height = 1


class AVLTree(BinarySearchTree[T]):

    # =========================
    # Altura
    # =========================

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    # =========================
    # Fator de Balanceamento
    # =========================

    def calculate_balance(self, node):
        if node is None:
            return 0

        return self._get_height(node.left) - self._get_height(node.right)

    # =========================
    # Rotação à Direita
    # =========================

    def right_rotation(self, z):
        y = z.left
        t3 = y.right

        y.right = z
        z.left = t3

        z.height = 1 + max(
            self._get_height(z.left),
            self._get_height(z.right)
        )

        y.height = 1 + max(
            self._get_height(y.left),
            self._get_height(y.right)
        )

        return y

    # =========================
    # Rotação à Esquerda
    # =========================

    def left_rotation(self, z):
        y = z.right
        t2 = y.left

        y.left = z
        z.right = t2

        z.height = 1 + max(
            self._get_height(z.left),
            self._get_height(z.right)
        )

        y.height = 1 + max(
            self._get_height(y.left),
            self._get_height(y.right)
        )

        return y

    # =========================
    # Rebalanceamento
    # =========================

    def rebalance(self, node, value=None, is_remove=False):

        balance = self.calculate_balance(node)

        # Esquerda-Esquerda
        if balance > 1 and (
            self.calculate_balance(node.left) >= 0
            if is_remove
            else value < node.left.data
        ):
            return self.right_rotation(node)

        # Direita-Direita
        if balance < -1 and (
            self.calculate_balance(node.right) <= 0
            if is_remove
            else value > node.right.data
        ):
            return self.left_rotation(node)

        # Esquerda-Direita
        if balance > 1 and (
            self.calculate_balance(node.left) < 0
            if is_remove
            else value > node.left.data
        ):
            node.left = self.left_rotation(node.left)
            return self.right_rotation(node)

        # Direita-Esquerda
        if balance < -1 and (
            self.calculate_balance(node.right) > 0
            if is_remove
            else value < node.right.data
        ):
            node.right = self.right_rotation(node.right)
            return self.left_rotation(node)

        return node

    # =========================
    # Atualiza altura e rebalanceia
    # =========================

    def rebalance_up(self, node, value=None, is_remove=False):

        if node is None:
            return None

        node.height = 1 + max(
            self._get_height(node.left),
            self._get_height(node.right)
        )

        return self.rebalance(node, value, is_remove)

    # =========================
    # Inserção
    # =========================

    def _insert(self, node, value):

        if node is None:
            return AVLNode(value)

        if value < node.data:
            node.left = self._insert(node.left, value)

        elif value > node.data:
            node.right = self._insert(node.right, value)

        else:
            return node

        return self.rebalance_up(node, value=value)

    # =========================
    # Remoção
    # =========================

    def _remove(self, node, value):

        if node is None:
            return None

        if value < node.data:

            node.left = self._remove(node.left, value)

        elif value > node.data:

            node.right = self._remove(node.right, value)

        else:

            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            successor = self._minimum(node.right)

            node.data = successor.data

            node.right = self._remove(node.right, successor.data)

        return self.rebalance_up(node, is_remove=True)