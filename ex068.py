from random import randint
v = 0
while True:
    num = int(input('digite um valor: '))
    computador = randint(0,10)
    total = num + computador
    tipo = ' '
    while tipo not in 'PI':
     tipo = str(input('voce quer ? P/I  ')).upper().strip()[0]
    print(f' voce jogou {num} e o computador jogou {computador} . o total é {total}')
    print(' DEU PAR 'if total % 2 == 0 else'DEU IMPAR')
    if tipo == 'P':
       if total % 2 ==0:
           print('VOCE VENCEU')
           v += 1
       else:
           print('VOCE PERDEU')
           break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCE VENCEU')
            v +=1
        else:
            print('VOCE PERDEU')
            break
        print('VAMOS JOGAR NOVAMENTE')
print('FIM DE JOGO, voce venceu {} vezes'.format(v))