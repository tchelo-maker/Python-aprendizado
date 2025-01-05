fut= dict()
partidas = list()
fut['nome']= str(input('Nome: '))
par = int(input('Quantas partidas ele jogou? '))
for c in range(par):
    partidas.append(int(input(f'{c+1} gol: ')))
fut['gols'] = partidas[:]
fut['total'] = sum(partidas)
print('-='*30)
print(fut)
for k , v in fut.items():
    print(f'O campo {k} tem o valor `{v}')
print('-='*30)
print(f'o jogador {fut["nome"]} jogou {len(fut["gols"])} partidas.')
for i , n in enumerate(fut['gols']):
    print(f'=> Na partida {i} fez {v} gols.')
print(f'Foi um total de {fut["total"]}gols.')