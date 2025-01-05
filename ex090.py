aluno = list()
notas = dict()
notas['nome'] = str(input('Nome: '))
notas['media'] = float(input(f'media de {notas['nome']}: '))
print(f'Media é igual {notas['media']}!')
if notas['media'] >= 7:
    print('Situação é igual a APROVADO(A)')
elif 5 <= notas['media'] < 7:
     print('Situação é igual RECUPERAÇÃO')
else:
    print('Situação é igual a REPROVADO(A)')
for k,v in notas.items():
    print(f'{k} = {v}')