valor = float(input('quaç é a distancia da sua viagem? '))
print(' voce esta prestes a começar a viagem de {}km.'.format(valor))
preco = valor * 0.50 if valor <= 200 else valor * 0.45
print('o valor da sua passagem deu R${}'.format(preco))