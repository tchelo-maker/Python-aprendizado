maior = 0
menor = 0
for p in range(1,6):
    n1 = float(input('peso da {} pessoa: '.format(p)))
    if p == 1:
       maior = p
       menor = p
    else:
        if n1 > maior:
            maior =  n1
        if n1 < menor:
         menor = n1
print(' o maior peso lido foi {} kg'.format(maior))
print('o menor peso lido foi de {}kg'.format(menor))