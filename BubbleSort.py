import random
import time

def BubbleSort(lista):
    n = len(lista)
    for i in range(n): # Percorrer todos os elementos da lista
        for j in range(0, n-i-1): # A última parte já estará ordenada, então o loop vai até n-i-1
            if lista[j] > lista[j+1]:
                # Troca se o elemento encontrado for maior que o próximo
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def odenado(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            print("não ordenado")
            break

lista_numeros = [random.randint(0, 50000) for _ in range(50000)]
#                                                        ^^^^^ quantidade de numeros na lista        
inicio_tempo = time.time()

lista_ordenada = BubbleSort(lista_numeros)

fim_tempo = time.time()
#print("Lista ordenada:", lista_ordenada)
odenado(lista_ordenada)
print(f"Tempo para ordenar: {fim_tempo - inicio_tempo:.9f} segundos")
