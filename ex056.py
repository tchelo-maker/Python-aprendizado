somaidade= 0
mediaidade = 0
maioridadehomem = 0
totmulher20 = 0
nomevelho= ' '
for p in range(1,5):
    print('------ {} pessoa ------'.format(p))
    nome = str(input('nome ')).strip()
    idade= int(input('idade: '))
    sexo =str(input('sexo [m/f] ')).strip()
    somaidade += idade
    if p == 1 and sexo == 'Mm':
       maioridadehomem = idade
       nomevelho = nome
    if sexo in 'Mm'and  idade > maioridadehomem:
       maioridadehomem = idade
       nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade= somaidade / 4
print('a media idade do grupo é {}anos '.format(mediaidade))
print('o home mais velho tem {} anos e se chama {} a'.format (maioridadehomem, nomevelho))
print('aao todo são {} mulheres com menos de 20 anos'.format(totmulher20))