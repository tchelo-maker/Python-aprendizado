ficha = list()
while True:
    nome = str(input('nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2 )/2
    ficha.append([nome, [nota1,nota2],media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*50)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-='*50)
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]}{a[2]:>8.1f}')
while True:
    print('-='*35)
    opc= int(input('Mostrar notas de qual aluno?(999 interrompe )'))
    if opc == 999:
        print('FINALIZAANDO...')
        break
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')


