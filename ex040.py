not1 = float(input('me informe sua nota. '))
not2 = float(input('me informe outra nota. '))
media = (not1 + not2)/2
if media <= 5:
    print('REPROVADO!')
elif media == 6:
    print('RECUPERAÇÃO')
elif media >= 6:
    print('PARABENS VOCE ESTA APROVADO')

