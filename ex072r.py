
cont = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')
while True:
    digite = int(input('Digite um numero: '))
    if 0<= digite <= 20:
     print(f'Voce digitou o numero {cont[digite]}')
     digite = str(input('Deseja continuar? ')).upper().strip()[0]
    if digite == 'N':
        break
    while digite != 'N' and digite != 'S':
     digite = str(input('Deseja continuar? ')).upper().strip()[0]




