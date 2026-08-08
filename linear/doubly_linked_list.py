"""Criando a lista duplamente encadeada"""

from typing import Generic, TypeVar, Optional

T = TypeVar("T")


class DoublyNode(Generic[T]):

    def __init__(self, data: T):

        self.data = data

        self.next: Optional["DoublyNode[T]"] = None

        self.prev: Optional["DoublyNode[T]"] = None



class DoublyLinkedList(Generic[T]):

    def __init__(self):

        self.head: Optional[DoublyNode[T]] = None

        self.tail: Optional[DoublyNode[T]] = None

        self._size = 0



    # Verifica se a lista está vazia
    def is_empty(self) -> bool:

        return self.head is None



    # Retorna quantidade de elementos
    def size(self) -> int:

        return self._size



    # Insere no início
    def insert_front(self, value: T) -> None:

        new_node = DoublyNode(value)


        if self.head is None:

            self.head = new_node

            self.tail = new_node


        else:

            new_node.next = self.head

            self.head.prev = new_node

            self.head = new_node


        self._size += 1



    # Insere no final
    def insert_end(self, value: T) -> None:

        new_node = DoublyNode(value)


        if self.tail is None:

            self.head = new_node

            self.tail = new_node


        else:

            new_node.prev = self.tail

            self.tail.next = new_node

            self.tail = new_node


        self._size += 1



    # Remove pelo valor
    def remove(self, value: T) -> bool:


        current = self.head


        while current is not None:


            if current.data == value:


                # Remove primeiro elemento
                if current.prev is None:

                    self.head = current.next


                else:

                    current.prev.next = current.next



                # Remove último elemento
                if current.next is None:

                    self.tail = current.prev


                else:

                    current.next.prev = current.prev



                self._size -= 1

                return True



            current = current.next



        return False



    # Busca elemento
    def search(self, value: T) -> bool:


        current = self.head


        while current is not None:


            if current.data == value:

                return True


            current = current.next



        return False



    # Percorre do início para o fim
    def display_forward(self) -> list[T]:


        result = []

        current = self.head


        while current is not None:

            result.append(current.data)

            current = current.next


        return result



    # Percorre do fim para o início
    def display_backward(self) -> list[T]:


        result = []

        current = self.tail


        while current is not None:

            result.append(current.data)

            current = current.prev


        return result



    # Limpa a lista
    def clear(self):

        self.head = None

        self.tail = None

        self._size = 0



    def __len__(self):

        return self._size



    def __str__(self):

        return str(self.display_forward())