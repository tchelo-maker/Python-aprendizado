todos =[[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o valor  {c} : '))
    if valor % 2 == 0:
       todos[0].append(valor)
    else:
        todos[1].append(valor)

print(f'numero pares {sorted(todos[0])}')
print(f'Numeros impares {sorted(todos[1])}')