num = int(input('digite um numero: '))
num2 = int(input('digite outro numero: '))
if num > num2:
    print('o numero {} é maior'.format(num))
elif num2 > num:
    print('o numero {} é maior'.format(num2))
elif num == num2:
    print('os dois numero são iguais ')