def soma (a, b):
      s = a * b
      print(s)

print()
print('CONTROLE DE TERRENO')
print('====================')

lar = float(input('Largura : '))
com = float(input('Comprimento: '))
print(f'A area de um terreno de {lar}x{com} é de ', end='')

soma(a=lar , b =com)


