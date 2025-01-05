salario = float(input('qual é o salario do funcionario? '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('quem ganhava R$ {} passa a ganhar R${} agora.'.format(salario, novo))