dias=int(input('quantos dia vou ficar com o carro alugado? '))
km=float(input('quantos km? '))
pago = (dias*60) + (km*0.15)
print('valor a ser pago R${:.1f}'.format(pago))