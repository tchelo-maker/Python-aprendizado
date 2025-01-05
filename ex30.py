num= int(input('digite um numero numero. '))
resultado = num % 2
if resultado == 0:
    print('o numero  \33[31m{}\33[m é par'.format(num))
else:
    print('o numero \33[32m{} é impar'.format(num))

