
pessoas = list()
dados = list()
mai = 0
men = 0
while True:
    pessoas.append(str(input('Nome:  ')))
    pessoas.append(float(input('Peso: ')))
    if len(dados) == 0 :
        mai = men = pessoas[1]
    else:
        if pessoas[1] > mai:
            mai = pessoas[1]
        if pessoas[1] < men:
            men = pessoas[1]
    dados.append(pessoas[:])
    pessoas.clear()
    es = str(input('Quer continuar [S/N]:  ')).upper().strip()
    if es == 'N':
        break
print(f'Foram cadastradas {len(dados)}')

print(f'O maior peso foi de  {mai}kg',end=' ')
for p in dados:
    if p[1] == mai:
        print(f'{p[0]}')
print(f' O menor peso foi de {men}kg', end=' ')
for p in dados:
    if p[1] == men:
        print(f'{p[0]}')