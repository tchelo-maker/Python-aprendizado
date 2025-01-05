from random import choice
al1=str(input('primeiro aluno: '))
al2=str(input('segundo aluno: '))
al3=str(input('terceiro aluno: '))
al4=str(input('quarto aluno: '))
lista =[al1,al2,al3,al4]
escolhido = choice(lista)
print('o escolhido foi {}'.format(escolhido))
