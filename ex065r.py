escolha = 'Ss'
negacao = 'Nn'
somar = 1
multiplicar = 2
print('BEM VINDO')
num = str(input('vamos jogar?: ')).upper()
while num in escolha :
    n1= int(input('escolha um numero: '))
    n2= int(input('escolha outro numero: '))
    print('''\033[41;30m<ESCOLHA UMA OPÇÃO>\033[m
    [1]somar
    [2]multiplicar''')
    deci = int(input('escolha uma opcão: '))
    if deci == somar:
     soma =  n1 + n2
     print('a soma entre o numeros é {} '.format(soma))
     break
    elif deci == multiplicar:
        multi = n1 * n2
        print('a multiplicação dos numero é {}'.format(multi))
        break
    else:
        print('ESCOLHA INVALIDA...')
print('ACABOU')
