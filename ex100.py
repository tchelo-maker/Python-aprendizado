from random import randint
from time import sleep
def sorteia(lista):
     print('SORTEANDO NUMEROS...')
     for cont in range(0,5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ',end='')
        sleep(0.5)
     print('PRONTO...')



def somapar(lista):
    soma=0
    for valor in lista:
        if  valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista} o resultado é {soma}')

numeros = list()
sorteia(numeros)
somapar(numeros)
