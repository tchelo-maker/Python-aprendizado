from time import sleep
lista = list()
cadastro = list()
print('-='*5 ,'CADASTRO DE EMPREGADO','=-'*5)
while True:
    lista.append ( str(input('Qual é seu nome:  ')))
    lista.append ( int(input('Qual é a sua idade : ')))
    lista.append (float(input('Digite o seu CPF: ')))
    cadastro.append(lista[:])
    lista.clear()
    escolha = str(input('Digite [s/n] se deseja continuar:  ')).upper().strip()
    if escolha == 'N':
        break
print(f'Foram cadastradas {len(cadastro)} pessoas')
print('='*50)
print('='*5,'FOLHA DE CADASTRO','='*5)
sleep(1)
print(f'>>>>>>NOME: {cadastro[0][0].upper()}')
print(f'>>>>>IDADE: {cadastro[0][1]}')
print(f'>>>>> CPF : {cadastro [0][2]:.0f}')
sleep(1)
print('>'*10,'CADASTRO FEITO COM SUCESSO','<'*10)