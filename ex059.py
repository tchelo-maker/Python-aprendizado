from time import sleep
n1 = int(input('digite um valor: '))
n2 = int (input('digite mais valor: '))
opcao=0
while opcao !=5:
    print('\033[31m===== MENU =====\033[m')
    print('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair do programa')
    opcao = int(input('escolha uma opção>: '))
    if opcao == 1:
        print('o resultado da soma é {} '.format(n1+n2))
    elif opcao == 2:
        print('o resultado da multiplição é {} '.format(n1*n2))
    elif opcao == 3:
        if n1 < n2:
            maior = n1
        else:
            maior = n2
        print('o maior é {}'.format(maior))
    elif opcao == 4:
        n1 = int(input('escolha novos valore: '))
        n2 = int(input('escolha mais um novo valor: '))
    elif opcao == 5:
        sleep(1)
        print('\033[41;30mFINALIZANDO...')
    else:
        print('opção invalida')
        sleep(1)
print('\033[41;30mFIM DO PROGRAMA\033[m')

