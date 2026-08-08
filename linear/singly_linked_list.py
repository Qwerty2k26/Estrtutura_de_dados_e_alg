"""Criando a lista encadeada simples"""

from typing import Generic, TypeVar, Optional

T = TypeVar("T")


class Node(Generic[T]):

    def __init__(self, data: T):
        self.data = data
        self.next: Optional["Node[T]"] = None



class SinglyLinkedList(Generic[T]):

    def __init__(self):
        self.head: Optional[Node[T]] = None
        self._size = 0


    # Verifica se a lista está vazia
    def is_empty(self) -> bool:
        return self.head is None


    # Retorna quantidade de elementos
    def size(self) -> int:
        return self._size


    # Insere no início da lista
    def insert_front(self, value: T) -> None:

        new_node = Node(value)

        new_node.next = self.head

        self.head = new_node

        self._size += 1



    # Insere no final da lista
    def insert_end(self, value: T) -> None:

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self._size += 1
            return


        current = self.head

        while current.next is not None:
            current = current.next


        current.next = new_node

        self._size += 1



    # Remove um elemento pelo valor
    def remove(self, value: T) -> bool:

        if self.head is None:
            return False


        # Caso seja o primeiro elemento
        if self.head.data == value:

            self.head = self.head.next

            self._size -= 1

            return True



        current = self.head


        while current.next is not None:

            if current.next.data == value:

                current.next = current.next.next

                self._size -= 1

                return True


            current = current.next


        return False



    # Busca um elemento
    def search(self, value: T) -> bool:

        current = self.head


        while current is not None:

            if current.data == value:
                return True

            current = current.next


        return False



    # Retorna os elementos da lista
    def display(self) -> list[T]:

        elements = []

        current = self.head


        while current is not None:

            elements.append(current.data)

            current = current.next


        return elements



    # Remove todos os elementos
    def clear(self):

        self.head = None

        self._size = 0



    def __len__(self):

        return self._size



    def __str__(self):

        return str(self.display())