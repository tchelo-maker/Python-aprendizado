frase = str(input('digite uma frase.  '))
print('a letra A aparece {} vezes'.format(frase.count('a')))
print('a letra A comeca em {} '.format(frase.find('a')+1))
print('a letra A termina em {} '.format(frase.rfind('a')+1))

