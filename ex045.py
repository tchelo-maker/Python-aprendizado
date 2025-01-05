from random import randint
from time import sleep
itens=('pedra','papel','tesoura')
computador = randint (0,2)
print('''suas opcções:
[0]pedra
[1]papel
[2]tesoura''')
voce= int(input('escolha um:  '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-'*20)
print('{}'.format(itens[computador]))
print('voce {}'.format(itens[voce]))
print('-'*20)
if computador == 0: # JOGOU PEDRA
    if voce == 0:
        print('EMPATE')
    elif voce == 1:
        print('VENCE')
    elif voce == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 1: # JOGOU PAPEL
    if voce == 0:
        print('VENCE')
    elif voce == 1:
        print('EMPATE')
    elif voce == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 2: # JOGOU TESOURA
    if voce == 0:
        print('VENCE')
    elif voce == 1:
        print('COMPUTADOR VENCE')
    elif voce == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')

