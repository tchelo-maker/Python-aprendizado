
print('============= BANCO NU ==============')
valor =  int(input('Qual é o valor que voce deseja sacar:  '))
total = valor
ced = 50
totced=0
while True:
    if total >= ced :
        total -= ced
        totced += 1
    else:
        if totced > 0:
           print('Total de {} cedulas de  R${} '.format(totced,ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*35)
print('FIM... TENHA UM BOM DIA ')