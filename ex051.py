print('-'*20)
print('10 TERMOS DE UMA PA')
print('-'*20)
num = int(input('primeiro termo:'))
razao = int(input('razão:'))
decimo = num + (10 - 1)* razao
if razao == 2 :
    for c in range(num,decimo, razao):
        print('{}'. format(c), end='  ')
print('ACABOU')