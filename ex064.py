num = cont = soma = 0
num = int(input('digite um numero [999 parar]:  '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('digite um numero [999 parar]:  '))
print('voce digitou {} numeros e a soma entre eles {}'.format(cont,soma))