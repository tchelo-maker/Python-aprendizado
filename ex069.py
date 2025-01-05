p = 0
homens18 =  0
homem=0
escolha = 'Ss'
mulheres = 0
while True:
    p += 1
    print('===== CADASTRO DA {} PESSOA ======'.format(p))
    print('='*35)
    idade = int(input('qual sua idade? '))
    sexo = ' '
    while sexo not in 'FM':
     sexo = str(input('qual seu sexo? M/F ')).strip().upper()[0]
    escolha = ' '
    while escolha not in 'SN':
     escolha =  str(input('Quer continuar? ')).upper().strip()[0]
    print('='*35)
    homens18 += idade > 18
    homem += sexo == 'm'
    mulheres += idade < 20

    if escolha not in  'Ss':
        break
print('PAROU')
print ('são {} homem com mais de 18 '.format(homens18))
print('são {} homens '.format(homem))
print('são {} mulher com menos de 20 '.format(mulheres))