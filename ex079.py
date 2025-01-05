valores = list ()
while True:
    n=(int(input('Digite um valor: ')))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor ja adicionado!')
    escolha= str(input('Quer continuar? s/n ' )).upper().strip()
    if escolha == 'N':
        break
valores.sort()
print(f'Os valores adicionados {valores}')