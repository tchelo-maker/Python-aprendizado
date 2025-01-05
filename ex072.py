
cont = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')
while True:
  digite = int(input('digite um numero entre 0 e 20: '))
  if 0 <= digite <= 20:
     break
  print('Tente novamente.')
print(f'Voce digitou o numero {cont[digite]}')
