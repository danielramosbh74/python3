# Fonte: https://algoritmosempython.com.br/cursos/algoritmos-python/pesquisa-ordenacao/insercao/
""" import random

def ordenacao_insercao(A):
    n = len(A)
    # Percorre o arranjo A.
    for j in range(1, n):
        chave = A[j]
        i = j - 1
        # Insere o elemento A[j] na posição correta.
        while i >= 0 and A[i] > chave:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = chave

A = random.sample(range(-10, 10), 10)

print("Arranjo não ordenado: ", A)
ordenacao_insercao(A)
print("Arranjo ordenado:", A) """


import random

A = random.sample(range(-10, 10), 5)

def ordenacao_insercao(A):
    n = len(A)
    print(n)
    print('---')
    # Percorre o arranjo A.
    for j in range(1, n):
        chave = A[j]
        print(j)
        print(chave)
        print()
        i = j - 1
        print(i)
        # Insere o elemento A[j] na posição correta.
        while i >= 0 and A[i] > chave:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = chave


print("Arranjo não ordenado: ", A)
ordenacao_insercao(A)
print("Arranjo ordenado:", A)
