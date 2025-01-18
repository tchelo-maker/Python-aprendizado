def ficha(jog='<Desconhecido>', gol=0):
    print(f'Jogador {jog} fez {gol} gols no campenatos')
n = str(input('Nome do jogador: '))
g = str(input('Numero de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)