from datetime import datetime
nota = dict()
nota['nome']= str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
nota['idade']= datetime.now().year - nasc
nota['ctps']=int(input('Carteira de trabalho: (0 não tem )'))
if nota['ctps'] != 0:
    nota['con']= int(input('Ano de contração'))
    nota['salario']= int(input('Salario: R$'))
    nota['apo']= nota['idade'] + ((nota['con']+35) - datetime.now().year)
print('-='*35)
for k,v in nota.items():
    print(f'- {k} tem o valor de {v}')