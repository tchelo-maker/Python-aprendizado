velocidade = float(input('qual é a velocidade do carro ? '))
if velocidade > 80:
    print('\33[31m MULTADO: voce foi multa')
    multa = (velocidade-80)*7
    print('voce deve pagar uma multa de R${:.2f}'.format(multa))
print ('tenha um bom dai dirija com segurança:')

