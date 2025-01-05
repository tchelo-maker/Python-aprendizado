valores = list()
while True:
     valores.append(int(input('Digite um numero: ')))
     escolha = str(input('Quer continuar? ')).upper().strip()
     if escolha == 'N':
        break
print(f'Foram digitados  {len(valores)} numeros ')
valores.sort(reverse=True)
print(f'O numeros em decrescente fica {valores}')
if 5 in valores:
    print('o valor 5 esta em lista')
else:
    print('ele não esta na lista')