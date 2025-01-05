print('='*20)
print('OS 10 PRIMEIROS TERMOS')
print('='*20)
num = int(input('Primeiro termo> '))
razao = int(input('Razão> '))
termo= num
cont = 1
while cont <= 10:
    print('{} > '.format(termo),end=' ')
    termo = termo + razao
    cont += 1
print('FIM')
