
while True:
       num = int(input('quer ver qual tabuada? '))
       if num < 0:
           break
       print('='*25)
       for c in range(1,11):
         soma = num * c
         print('    {} x {} = {} '.format(num,c,soma))
       print('='*25)
print('  ...PROGRAMA FINALIZADO...')


