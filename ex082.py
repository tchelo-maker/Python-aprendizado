valores = list()
pares = list()
impares = list()
while True:
    num = int(input('Digite um valor: '))
    if num % 2 ==0:
        pares.append(num)
    else:
        impares.append(num)
    valores.append(num)
    escolhar = str(input('Quer continuar? S/N  ')).upper().strip()
    if escolhar == 'N':
        break

print(f'{valores}')
print(f'{pares}')
print(f'{impares}')