from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    n1 = int(input('em que ano a {} pessoa nasceu? '.format(pess)))
    conta = atual - n1
    if conta >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('TOTAL tem {} pessoa menor de idade e {} maiores de idade'.format(totmenor,totmaior))
