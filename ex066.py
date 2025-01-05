num = 0
soma = 0
quant = 0
while True:
    num = int(input('digite um numero: '))
    if num == 999:
        break
    soma += num
    quant += 1
print('foi digitado {}'.format(quant))
print('a soma desses numero é {}'.format(soma))