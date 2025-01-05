n1 = int(input('digite um valor.  '))
c = n1
f = 1
print('calculando {}! ='.format(n1),end=' ')
for c in range(0,6):
    print('{} '.format(c),end=' ')
    print('x'if c > 1 else '=', end=' ')
    f*= c
    c-=1
print('{}'.format(f))
#print('o factorial de {} é {}'.format(n1,soma))#
