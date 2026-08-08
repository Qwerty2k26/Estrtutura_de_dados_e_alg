"""Criando o nó para as arvores"""

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class TreeNode(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.left: Optional["TreeNode[T]"] = None       #(None <-left <----[raiz]----> rigth-> None)
        self.right: Optional["TreeNode[T]"] = None