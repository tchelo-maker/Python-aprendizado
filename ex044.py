valor = float(input('qual o valor a ser pago do produto? '))
print('o valor normal do produto é R${} '.format(valor))
print('-'*20)
print(' avista \n avista no catão \n parcelado')
print('-'*20)
metodo = str(input('qual seu metodo de pagamento? '))
produto = (( valor * 10) / 100 )
resul = valor - produto
produto2 = ((valor * 5 ) /100)
resul2 = valor - produto2
produto3 = (valor * 20)/100
resul3 = valor + produto3
if metodo == 'avista' :
    print('o valor do produto vai ficar a vista no dinheiro R${}'.format(resul))
elif metodo == 'avista no cartão':
    print('o valor avista no cartão fica R${} '.format(resul2))
elif metodo == 'parcelado':
    vezes=float(input('quantas vezes? '))
    parcelas = resul3 / vezes
    print('o valor ficar R${} de R${} em {:.0f} vezes'.format(resul3,parcelas,vezes))