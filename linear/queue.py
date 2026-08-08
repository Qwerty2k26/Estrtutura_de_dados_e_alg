"""Criando a classe da Fila"""

from typing import Generic, TypeVar

T = TypeVar("T")

#Fila
class Queue(Generic[T]):

    def __init__(self):
        self._data: list[T] = []


    # Verifica se a fila está vazia
    def is_empty(self) -> bool:
        return len(self._data) == 0


    # Insere um elemento no final da fila
    def enqueue(self, value: T) -> None:
        self._data.append(value)


    # Remove e retorna o primeiro elemento da fila
    def dequeue(self) -> T:
        if self.is_empty():
            raise IndexError("A fila está vazia.")

        return self._data.pop(0)


    # Visualiza o primeiro elemento da fila
    def front(self) -> T:
        if self.is_empty():
            raise IndexError("A fila está vazia.")

        return self._data[0]


    # Visualiza o último elemento da fila
    def rear(self) -> T:
        if self.is_empty():
            raise IndexError("A fila está vazia.")

        return self._data[-1]


    # Retorna a quantidade de elementos
    def size(self) -> int:
        return len(self._data)


    # Remove todos os elementos
    def clear(self) -> None:
        self._data.clear()


    # Retorna uma cópia dos elementos
    def display(self) -> list[T]:
        return self._data.copy()


    # Permite usar len(fila)
    def __len__(self):
        return len(self._data)


    # Impressão da fila
    def __str__(self):
        return str(self._data)