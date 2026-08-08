from linear.stack import Stack
from linear.queue import Queue
from linear.singly_linked_list import SinglyLinkedList
from linear.doubly_linked_list import DoublyLinkedList

from trees.binary_search_tree import BinarySearchTree
from trees.avl import AVLTree
from trees.b_tree import BTree


# =====================================================
# INSTÂNCIAS DAS ESTRUTURAS
# =====================================================

pilha = Stack[int]()

fila = Queue[int]()

lista_simples = SinglyLinkedList[int]()

lista_dupla = DoublyLinkedList[int]()

bst = BinarySearchTree[int]()

avl = AVLTree[int]()

arvore_b = BTree[int](2)



# =====================================================
# MENU PRINCIPAL
# =====================================================

def menu_principal():

    while True:

        print("""
==============================
 SISTEMA DE ESTRUTURAS DE DADOS
==============================

1 - Estruturas Lineares
2 - Árvores
0 - Sair
""")


        opcao = input("Escolha uma opção: ")


        if opcao == "1":
            menu_lineares()


        elif opcao == "2":
            menu_arvores()


        elif opcao == "0":
            print("Programa encerrado.")
            break


        else:
            print("Opção inválida!")



# =====================================================
# MENU LINEARES
# =====================================================

def menu_lineares():

    while True:

        print("""
========== ESTRUTURAS LINEARES ==========

1 - Pilha
2 - Fila
3 - Lista Encadeada Simples
4 - Lista Duplamente Encadeada
0 - Voltar
""")


        opcao = input("Escolha uma opção: ")


        if opcao == "1":
            menu_pilha()


        elif opcao == "2":
            menu_fila()


        elif opcao == "3":
            menu_lista_simples()


        elif opcao == "4":
            menu_lista_dupla()


        elif opcao == "0":
            break


        else:
            print("Opção inválida!")



# =====================================================
# MENU PILHA
# =====================================================

def menu_pilha():

    while True:

        print("""
============== PILHA ==============

1 - Inserir elemento
2 - Remover elemento
3 - Ver topo
4 - Mostrar elementos
5 - Ver tamanho
0 - Voltar
""")


        opcao = input("Escolha uma opção: ")



        if opcao == "1":

            valor = int(input("Valor: "))

            pilha.push(valor)

            print("Elemento inserido.")



        elif opcao == "2":

            removido = pilha.pop()

            print("Removido:", removido)



        elif opcao == "3":

            print("Topo:", pilha.top())



        elif opcao == "4":

            print("Pilha:", pilha.display())



        elif opcao == "5":

            print("Quantidade:", pilha.size())



        elif opcao == "0":

            break


        else:

            print("Opção inválida!")
            
            

# =====================================================
# MENU FILA
# =====================================================

def menu_fila():

    while True:

        print("""
============== FILA ==============

1 - Inserir elemento
2 - Remover elemento
3 - Ver primeiro elemento
4 - Ver último elemento
5 - Mostrar elementos
6 - Ver tamanho
0 - Voltar
""")


        opcao = input("Escolha uma opção: ")


        if opcao == "1":

            valor = int(input("Valor: "))

            fila.enqueue(valor)

            print("Elemento inserido.")



        elif opcao == "2":

            removido = fila.dequeue()

            print("Removido:", removido)



        elif opcao == "3":

            print("Primeiro:", fila.front())



        elif opcao == "4":

            print("Último:", fila.rear())



        elif opcao == "5":

            print("Fila:", fila.display())



        elif opcao == "6":

            print("Quantidade:", fila.size())



        elif opcao == "0":

            break


        else:

            print("Opção inválida!")


# =====================================================
# MENU LISTA SIMPLES
# =====================================================

def menu_lista_simples():

    while True:

        print("""
======= LISTA ENCADEADA SIMPLES =======

1 - Inserir no final
2 - Remover elemento
3 - Buscar elemento
4 - Mostrar lista
5 - Ver tamanho
0 - Voltar
""")


        opcao = input("Escolha uma opção: ")



        if opcao == "1":

            valor = int(input("Valor: "))

            lista_simples.insert_end(valor)

            print("Elemento inserido.")



        elif opcao == "2":

            valor = int(input("Valor para remover: "))

            lista_simples.remove(valor)

            print("Elemento removido.")



        elif opcao == "3":

            valor = int(input("Valor para buscar: "))

            resultado = lista_simples.search(valor)

            print("Encontrado:", resultado)



        elif opcao == "4":

            print("Lista:", lista_simples.display())



        elif opcao == "5":

            print("Quantidade:", lista_simples.size())



        elif opcao == "0":

            break


        else:

            print("Opção inválida!")





# =====================================================
# MENU LISTA DUPLA
# =====================================================

def menu_lista_dupla():

    while True:

        print("""
======= LISTA DUPLAMENTE ENCADEADA =======

1 - Inserir no final
2 - Remover elemento
3 - Mostrar frente
4 - Mostrar trás
5 - Ver tamanho
0 - Voltar
""")


        opcao = input("Escolha uma opção: ")



        if opcao == "1":

            valor = int(input("Valor: "))

            lista_dupla.insert_end(valor)

            print("Elemento inserido.")



        elif opcao == "2":

            valor = int(input("Valor para remover: "))

            lista_dupla.remove(valor)

            print("Elemento removido.")



        elif opcao == "3":

            print(
                "Frente:",
                lista_dupla.display_forward()
            )



        elif opcao == "4":

            print(
                "Trás:",
                lista_dupla.display_backward()
            )



        elif opcao == "5":

            print(
                "Quantidade:",
                lista_dupla.size()
            )



        elif opcao == "0":

            break


        else:

            print("Opção inválida!")
            

# =====================================================
# MENU ÁRVORES
# =====================================================

def menu_arvores():

    while True:

        print("""
============== ÁRVORES ==============

1 - Árvore Binária de Busca (BST)
2 - AVL
3 - Árvore B
0 - Voltar
""")


        opcao = input("Escolha uma opção: ")


        if opcao == "1":

            menu_bst()


        elif opcao == "2":

            menu_avl()


        elif opcao == "3":

            menu_arvore_b()


        elif opcao == "0":

            break


        else:

            print("Opção inválida!")




# =====================================================
# MENU BST
# =====================================================

def menu_bst():

    while True:

        print("""
========== ÁRVORE BST ==========

1 - Inserir elemento
2 - Remover elemento
3 - Buscar elemento
4 - Mostrar em ordem
5 - Mostrar pré ordem
6 - Mostrar pós ordem
7 - Altura
8 - Quantidade de nós
0 - Voltar
""")


        opcao = input("Escolha uma opção: ")



        if opcao == "1":

            valor = int(input("Valor: "))

            bst.insert(valor)

            print("Inserido.")



        elif opcao == "2":

            valor = int(input("Valor para remover: "))

            bst.remove(valor)

            print("Removido.")



        elif opcao == "3":

            valor = int(input("Valor para buscar: "))

            resultado = bst.search(valor)


            if resultado:

                print("Encontrado:", resultado.data)

            else:

                print("Não encontrado.")



        elif opcao == "4":

            print(
                "Em ordem:",
                bst.in_order()
            )



        elif opcao == "5":

            print(
                "Pré ordem:",
                bst.pre_order()
            )



        elif opcao == "6":

            print(
                "Pós ordem:",
                bst.post_order()
            )



        elif opcao == "7":

            print(
                "Altura:",
                bst.height()
            )



        elif opcao == "8":

            print(
                "Quantidade:",
                bst.size()
            )



        elif opcao == "0":

            break


        else:

            print("Opção inválida!")





# =====================================================
# MENU AVL
# =====================================================

def menu_avl():

    while True:

        print("""
============== AVL ==============

1 - Inserir elemento
2 - Remover elemento
3 - Buscar elemento
4 - Mostrar em ordem
5 - Mostrar pré ordem
6 - Altura
7 - Quantidade de nós
0 - Voltar
""")


        opcao = input("Escolha uma opção: ")



        if opcao == "1":

            valor = int(input("Valor: "))

            avl.insert(valor)

            print("Inserido.")



        elif opcao == "2":

            valor = int(input("Valor para remover: "))

            avl.remove(valor)

            print("Removido.")



        elif opcao == "3":

            valor = int(input("Valor para buscar: "))

            resultado = avl.search(valor)


            if resultado:

                print("Encontrado:", resultado.data)

            else:

                print("Não encontrado.")



        elif opcao == "4":

            print(
                "Em ordem:",
                avl.in_order()
            )



        elif opcao == "5":

            print(
                "Pré ordem:",
                avl.pre_order()
            )



        elif opcao == "6":

            print(
                "Altura:",
                avl.height()
            )



        elif opcao == "7":

            print(
                "Quantidade:",
                avl.size()
            )



        elif opcao == "0":

            break


        else:

            print("Opção inválida!")





# =====================================================
# MENU ÁRVORE B
# =====================================================

def menu_arvore_b():

    while True:

        print("""
============== ÁRVORE B ==============

1 - Inserir elemento
2 - Buscar elemento
3 - Mostrar níveis
4 - Altura
5 - Quantidade de chaves
0 - Voltar
""")


        opcao = input("Escolha uma opção: ")



        if opcao == "1":

            valor = int(input("Valor: "))

            arvore_b.insert(valor)

            print("Inserido.")



        elif opcao == "2":

            valor = int(input("Valor para buscar: "))

            resultado = arvore_b.search(valor)


            if resultado:

                no, posicao = resultado

                print("Encontrado no nó:", no.keys)

                print("Posição:", posicao)

            else:

                print("Não encontrado.")



        elif opcao == "3":

            arvore_b.print_levels()



        elif opcao == "4":

            print(
                "Altura:",
                arvore_b.height()
            )



        elif opcao == "5":

            print(
                "Quantidade:",
                arvore_b.size()
            )



        elif opcao == "0":

            break


        else:

            print("Opção inválida!")





# =====================================================
# INÍCIO DO PROGRAMA
# =====================================================

if __name__ == "__main__":

    menu_principal()