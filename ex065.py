resp = 'S'
soma = quant= media = maior = menor = 0
while resp in  'Ss':
    num= int(input('digite um valor: '))
    soma += num
    quant += 1
    if quant == 1:
        maior= menor= num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('quer continuar? s/n:  ')).upper().strip()
media = soma / quant
print('voce digitou {} numeros e a  media foi {} '.format(quant,media))
print('o numero menor foi {} e o maior {} '.format(menor,maior))
