"""
-> é uma lista de listas de numeros inteiros
-> as listas internas tem o tamanho de 10 elementos
-> as listas internas contem numeros entre 1 a 10 e eles
podem ser duplicados

Exercicio

-> Crie uma função que controla o primeiro duplicado considerando
o segundo numero como a duplicação:
    requisitos:
        A ordem do numero duplicado é considerada a partir
        da segunda ocorrencia do numero, ou seja, o numero duplicado em si.
        Exemplo: [1, 2, 3, ->3<-, 2, 1] 
        >> 1, 2 e 3 são duplicados
        Se não encontrar duplicadaos na lista, retorne -1
"""

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 3, 5, 7, 2, 4, 6, 8, 10],
    [5, 4, 2, 3, 10, 6, 8, 9, 7, 1],
    [8, 7, 3, 7, 5, 6, 7, 8, 9, 10],
    [5, 1, 6, 5, 7, 6, 4, 6, 8, 10],
    [5, 4, 5, 5, 6, 6, 8, 9, 7, 10],
    [5, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 3, 3, 7, 2, 4, 6, 8, 3],
    [5, 4, 2, 2, 1, 6, 8, 9, 7, 10],
    [1, 2, 3, 4, 5, 6, 6, 8, 9, 6],
    [9, 1, 2, 5, 1, 1, 4, 6, 8, 10],
    [5, 4, 1, 1, 2, 2, 8, 1, 7, 10],
]

def encontra_primeiro_duplicado(param_lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in param_lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)

    return primeiro_duplicado

for lista_de_inteiros in lista_de_listas_de_inteiros:
    print(lista_de_inteiros, encontra_primeiro_duplicado(lista_de_inteiros))

