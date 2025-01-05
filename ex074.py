from random import randint
numeros = (randint (1,10), randint(1, 10), randint(1,10), randint(1,10),randint(1,10))
print ('Os valores sorteados foram: ', end=' ')
for n in numeros:
    print(f'{n}',end=' ')

print(f'\no maior valor sorteado foi {max(numeros)}')
print(f'o menor valor sorteado foi {min(numeros)}')

