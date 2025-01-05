num = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))
num4 = int(input('Digite um numero: '))
tupla = (num,num2,num3,num4)
print(f'A primeira posição do numero 3 foi {tupla.count(9)}')
if 3 in tupla:
 print(f'A primeira posição do numero tres é {tupla.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end = ' ')
for n  in tupla:
    if n % 2 ==0:
        print(n, end=' ')



