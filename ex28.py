from random import randint
from time import sleep
computador = randint (0,5) #faz o computador pensa" Pensar"
print('-=- '* 10)
print(' vou pensar em um numero entre 0 e 5.tente adivinhar...')
print('-=- '* 10)
jogador = int(input(' em que numero eu pensei? ')) #jogador tenta adivinhar
print("\33[33mPROCESSANDO...")
sleep(3)
if jogador == computador:
    print('parabens voçe conseguiu me vencer')
else:
    print('ganhei! hahahaha'.format((computador,jogador)))