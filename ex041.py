from datetime import date
atual = date.today().year
nascimento = int(input('qual seu ano de nascimento?'))
cal = atual - nascimento
print(' o atleta tem {} '.format(cal))
if cal <= 9:
     print('classificação mirim')
elif  cal <= 14:
     print('classificação infantil')
elif cal <= 19:
    print('classificação junior')
elif cal <= 25:
    print('classificação senior')
else:
    print('classificação master')