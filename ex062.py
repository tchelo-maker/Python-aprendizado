print('='*20)
print('10 PRIMEIROS TERMOS')
print('='*20)
num = int(input('digite um termo> '))
razao = int(input('digite uma razão> '))
termo = num
cont =1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}>'.format(termo),end=' ')
        termo += razao
        cont +=1
    print('PAUSA')
    mais= int(input('quer mais quantos termos? '))
print(' preocesso finalizado com {} termos mostrados '.format(total))