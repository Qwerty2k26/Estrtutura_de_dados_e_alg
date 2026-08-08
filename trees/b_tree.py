"""Implementação da Árvore B."""

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class BTreeNode(Generic[T]):
    """Nó da Árvore B."""

    def __init__(self, leaf: bool = True):
        self.leaf = leaf
        self.keys: list[T] = []
        self.children: list["BTreeNode[T]"] = []


class BTree(Generic[T]):
    """Implementação de uma Árvore B."""

    def __init__(self, t: int):
        self.root = BTreeNode(True)
        self.t = t

    # =========================
    # Busca
    # =========================

    def search(self, key: T, node: Optional[BTreeNode[T]] = None):

        if node is None:
            node = self.root

        i = 0

        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return node, i

        if node.leaf:
            return None

        return self.search(key, node.children[i])

    # =========================
    # Split
    # =========================

    def split(self, parent: BTreeNode[T], index: int):

        t = self.t

        full = parent.children[index]

        new = BTreeNode(full.leaf)

        # A chave do meio sobe
        middle_key = full.keys[t - 1]

        # O novo nó recebe as maiores chaves
        new.keys = full.keys[t:]

        # O antigo fica com as menores
        full.keys = full.keys[: t - 1]

        # Divide os filhos
        if not full.leaf:
            new.children = full.children[t:]
            full.children = full.children[:t]

        # Atualiza o pai
        parent.children.insert(index + 1, new)
        parent.keys.insert(index, middle_key)

    # =========================
    # Inserção
    # =========================

    def insert(self, key: T):

        root = self.root

        if len(root.keys) == (2 * self.t - 1):

            new_root = BTreeNode(False)

            new_root.children.append(root)

            self.root = new_root

            self.split(new_root, 0)

            self._insert_non_full(new_root, key)

        else:

            self._insert_non_full(root, key)

    def _insert_non_full(self, node: BTreeNode[T], key: T):

        i = len(node.keys) - 1

        if node.leaf:

            node.keys.append(key)

            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1

            node.keys[i + 1] = key

        else:

            while i >= 0 and key < node.keys[i]:
                i -= 1

            i += 1

            # Divide o filho antes de descer
            if len(node.children[i].keys) == (2 * self.t - 1):

                self.split(node, i)

                if key > node.keys[i]:
                    i += 1

            self._insert_non_full(node.children[i], key)

    # =========================
    # Altura
    # =========================

    def height(self, node=None):

        if node is None:
            node = self.root

        if node.leaf:
            return 0

        return 1 + self.height(node.children[0])

    # =========================
    # Quantidade de chaves
    # =========================

    def size(self, node=None):

        if node is None:
            node = self.root

        total = len(node.keys)

        if not node.leaf:

            for child in node.children:
                total += self.size(child)

        return total

    # =========================
    # Impressão por níveis
    # =========================

    def print_levels(self):

        if not self.root.keys:
            print("Árvore vazia.")
            return

        queue = [(self.root, 0)]
        current_level = 0

        print("--- Estrutura da Árvore B ---")

        while queue:

            node, level = queue.pop(0)

            if level != current_level:
                current_level = level
                print()

            print(f"Nível {level}: {node.keys}")

            if not node.leaf:
                for child in node.children:
                    queue.append((child, level + 1))