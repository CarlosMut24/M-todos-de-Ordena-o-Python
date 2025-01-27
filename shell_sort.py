import time
import random
def ShellSort(lista):
    n = len(lista)
    gap = n // 2  # Inicialmente o gap é metade do tamanho da lista
    while gap > 0:
        for i in range(gap, n): # Fazer a ordenação por inserção para os elementos com o gap atual
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp: # Comparar elementos a gap posições de distância
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 2  # Reduzir o gap pela metade
    return lista

def odenado(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            print("não ordenado")
            break
lista_numeros = [random.randint(0, 50000) for _ in range(50000)]
#                                                        ^^^^^ quantidade de numeros na lista        
inicio_tempo = time.time()

lista_ordenada = ShellSort(lista_numeros)

fim_tempo = time.time()
#print("Lista ordenada:", lista_ordenada)
odenado(lista_ordenada)
print(f"Tempo para ordenar: {fim_tempo - inicio_tempo:.9f} segundos")
