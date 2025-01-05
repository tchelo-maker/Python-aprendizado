tuplas = ('marcelo','naty','carro','python')
for p in tuplas:
    print(f'\nNa palavra {p.upper()} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')