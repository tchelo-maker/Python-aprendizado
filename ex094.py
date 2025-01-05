pesso = dict()
lista = list()
soma = media = 0
while True:
  pesso.clear()
  pesso ['nome']=str(input('Nome: '))
  while True:
      pesso['sexo']=str(input('Sexo: m/f= ')).upper().strip()[0]
      if pesso['sexo'] in 'MmFf':
          break
      print('ERRO INVALID')
  pesso['idade']=int(input('Idade: '))
  soma += pesso['idade']
  lista.append(pesso.copy())
  while True:
      escolha = str(input('Quer continuar cadastrando: s/n  ')).upper().strip()
      if escolha in 'SN':
         break
      print('RESPONDA APENAS S OU N.')
  if escolha =='N':
    break
print('-='*30)
print(lista)
print(f'Ao todo temos {len(lista)} pessoa cadastrada!')
media = soma / len(lista)
print(f'A media de idade é de {media:5.2f} anos ')
print('As mulhers cadastradas foram', end=' ')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}',end='')
print()
print('pessoas a cima da media: ',end='')
for p in lista:
    if p['idade']>=  media:
        print('  ')
        for k,v in p.items():
            print(f'{k} = {v}; ',end='')
        print()
print('<< ENCERRANDO >>')
