from random import randint
from time import sleep
lista = list()
jogos = list()
print('-='*30)
print('     JOGA NA MEGA SENA     ')
print('-='*30)
quant = int(input('Quantos jogos voce quer que eu sorteie?  '))
tot = 0
while tot <= quant:
    cont=0
    while True:
        rando = randint(1,60)
        if rando not in lista:
            lista.append(rando)
            cont+=1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('='*3,f'SORTEANDO {quant} JOGOS','='*3)
for i,l in enumerate (jogos):
    print(f'jogo {i+1}:{l}')
    sleep(1)
print('+='*5,'BOA SORTE!','+='*5)

