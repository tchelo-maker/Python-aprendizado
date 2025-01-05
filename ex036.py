emprestimo = float(input('qual o valor do emprestimo que voce quer? '))
salario = float(input('quanto voce ganha? '))
anos = int(input('em quantos anos vai fazer? '))
vezes = emprestimo/(anos*12)
minimo = salario * 30 / 100
print('suas prestacões vão ficar {} em {} '.format(vezes,anos ))
if vezes <= minimo:
     print('emprestimo vai ser concedido!')
else:
     print('EMPRESTIMO NEGAD0')
