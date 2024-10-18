import time
import random

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[len(lista) // 2]  # Definir o pivô no meio da lista
        esquerda = [x for x in lista if x < pivot]  # Elementos menores que o pivô
        meio = [x for x in lista if x == pivot]  # Elementos iguais ao pivô
        direita = [x for x in lista if x > pivot]  # Elementos maiores que o pivô
        return quick_sort(esquerda) + meio + quick_sort(direita)

def odenado(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            print("não ordenado")
            break

lista_numeros = [random.randint(0, 50000) for _ in range(50000)]
#                                                        ^^^^^ quantidade de numeros na lista        

inicio_tempo = time.time()

lista_ordenada = quick_sort(lista_numeros)

fim_tempo = time.time()

#print("Lista ordenada:", lista_ordenada)
odenado(lista_ordenada)
print(f"Tempo para ordenar: {fim_tempo - inicio_tempo:.9f} segundos")
