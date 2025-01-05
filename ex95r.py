fut= dict()
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
        escolha = str(input('Quer continuar? ')).upper().strip()[0]
        if escolha in 'SN':
            break
        print('INVALID')
    if escolha == 'N':
        break
print('-='*35)
print('cod',end='')
for i in fut.keys:
    print(f'{i:<15}',end='')
print()
print('-='*30)
for k , v  in enumerate (time):
    print(f'{k:>15}')



