matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = mai = scol = 0
for l in range (0,3):
    for c in range(0,3):
        matriz [l] [c] =int(input(f'Digite o valor[{l},{c}]: '))
print('='*50)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]')
        if matriz [l] [c]% 2 ==0:
            spar += matriz[l][c]
    print('')
print('+='*50)
print(f'A soma dos valores pares é {spar}')
for l in range (0,3):
    scol +=matriz[l][2]
print(f'A soma dos valores da 3 coluna é {scol}')
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz [1][c]:
        mai = matriz [1][c]
print(f'O maior valor é {mai}')