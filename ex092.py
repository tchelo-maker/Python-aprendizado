from datetime import datetime
nota = dict()
nota['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
nota['idade'] = datetime.now().year - nasc
nota['carteira'] = int(input('carteira de trabalho: (0 não tem) '))
if nota['carteira'] !=0:
    nota['con']= int(input('Ano de contratação: '))
    nota['sala'] = float(input('Salario: R$'))
    nota['apo']= nota['idade'] + ((nota ['con'] + 35) - datetime.now().year)
print('-='*30)
for k , v in nota.items():
    print(f' -{k} tem o valor {v}')
