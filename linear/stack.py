"""Criando a classe da pilha"""

from typing import Generic, TypeVar

T = TypeVar("T")

#Pilha
class Stack(Generic[T]):
    def __init__(self):
        self._data: list[T] = []

    # Verifica se a pilha está vazia
    def is_empty(self) -> bool:
        return len(self._data) == 0

    # Insere um elemento no topo
    def push(self, value: T) -> None:
        self._data.append(value)

    # Remove e retorna o elemento do topo
    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("A pilha está vazia.")

        return self._data.pop()

    # Retorna o topo sem remover
    def top(self) -> T:
        if self.is_empty():
            raise IndexError("A pilha está vazia.")

        return self._data[-1]

    # Retorna a quantidade de elementos
    def size(self) -> int:
        return len(self._data)

    # Esvazia a pilha
    def clear(self) -> None:
        self._data.clear()

    # Retorna os elementos da pilha
    def display(self) -> list[T]:
        return self._data.copy()

    # Permite usar len(pilha)
    def __len__(self):
        return len(self._data)

    # Impressão da pilha
    def __str__(self):
        return str(self._data)