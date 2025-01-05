print('='*35)
print('Sequencia de fibonacci')
print('='*35)
n1 = int(input('quantos termos voce quer mostrar: '))
t1 = 0
t2 = 1
print('~'*35)
print('{} {}'.format(t1,t2),end=' ')
cont= 3
while cont <= n1:
    t3= t1 + t2
    print('{}'.format(t3),end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')