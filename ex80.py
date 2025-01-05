valores = list()
for c in range(0,5):
    num = int(input('Digite um valor: '))
    if c ==0 :
     valores.append(num)
     print('adicionado ao final da listas...')
    elif num > valores[-1]:
        valores.append(num)
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos , num)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1

print(f'{valores}')
