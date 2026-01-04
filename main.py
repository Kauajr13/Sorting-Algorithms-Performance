import random
import time
import copy

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from heap_sort import heap_sort

def testar_algoritmo(nome, funcao, vetor):
    copia = copy.deepcopy(vetor)
    inicio = time.perf_counter()
    funcao(copia)
    fim = time.perf_counter()
    return (nome, fim - inicio)

def gerar_vetores(n):
    crescente = list(range(n))
    decrescente = list(range(n, 0, -1))
    aleatorio = [random.randint(0, n) for _ in range(n)]
    return crescente, decrescente, aleatorio

algoritmos = [
    ("Bubble Sort", bubble_sort),
    ("Insertion Sort", insertion_sort),
    ("Merge Sort", merge_sort),
    ("Quick Sort", quick_sort),
    ("Heap Sort", heap_sort)
]

tamanhos = [10, 100, 1000, 5000]

for n in tamanhos:
    print(f"\nTamanho do vetor: {n}")
    tipos = ["Crescente", "Decrescente", "Aleatório"]
    vetores = gerar_vetores(n)

    for tipo, vetor in zip(tipos, vetores):
        print(f"\n  Entrada: {tipo}")
        for nome, funcao in algoritmos:
            nome_alg, tempo = testar_algoritmo(nome, funcao, vetor)
            print(f"    {nome_alg:<15}: {tempo:.6f} segundos")
