peso = float(input('qual seu peso?  '))
altura = float(input(' qual sua altura? '))
imc = peso / (altura ** 2)
print('seu imc é de {} '.format(imc))
if imc < 18.5:
    print('esta abaixo do peso')
elif   18.5 <= imc < 25:
    print('peso ideal')
elif 25 <= imc < 30:
    print('sobrepeso')
elif 30 <= imc < 40:
    print('obesidade')
else:
    print('obesidade morbida')