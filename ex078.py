mai = 0
men = 0

valores = list()
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        mai = men = valores[cont]
    else:
        if valores[cont] > mai:
            mai = valores [cont]
        if valores[cont]< men:
            men = valores[cont]

print('+='*50)
print(f'Os valores digitados foram {valores}')


print(f'Os maiors valores {mai} e estão na posição ', end=' ')
for i,v in enumerate(valores):
    if v == mai:
        print(f'{i}...')
print()
print(f'os menores valores {men} e estão na posição ', end= ' ')
for e,p in enumerate(valores):
    if p == men :
        print(f'{e}...')
        print()

print('+='*50)