ano = int(input('me informe seu ano de nascimento! '))
idade = (ano-2024)+18
if idade == 0:
     print('já é hora de se alistar ')
     print('SE ALISTA AGORA')
elif idade >=1:
    print('ainda vai se alisatar ')
    print('FALTA {} ANOS PARA SE ALISTAR'.format(idade))
elif idade <= -1:
    print('ja passou da hora de  se alistar')
    print('JA DEVIA TER SE ALISTADO!!')

