fut = dict()
partidas = list()
time = list()
while True:
    fut.clear()
    fut['nome']= str(input('Nome: '))
    par = int(input('Quantas partidas ele jogou? '))
    partidas.clear()
    for c in range(par):
        partidas.append(int(input(f'{c+1} gol: ')))
    fut['gols'] = partidas[:]
    fut['total'] = sum(partidas)
    time.append(fut.copy())
    while True:
        escolha = str(input('Quer continuar: s/n  ')).upper().strip()[0]
        if escolha in 'SN':
            break
        print('RESPOSTA INVALID')
    if escolha == 'N':
          break
print('-='*30)
print('cod',end='')
for i in fut.keys():
    print(f'{i:<15}', end='')
print()
print('-='*30)
for k ,v in enumerate (time):
    print(f' {k:>3} ' , end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*30)
while True:
    busca = int(input('mostrar dados de qual jogador? (999 para Parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com com codigo da {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f' No jogo {i} fez {g} gols')
    print('-'*30)
print('<< VOLTE SEMPRE >>')


