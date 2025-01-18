from datetime import date
def ano (num):
    s =  date.today().year - num
    print(f'Voce tem {s} anos| ', end='')
    if (s >= 16) and (s <= 17) :
         print(' VOTO OPCIONAL')
    elif s >= 60 :
        print('VOTO OPCIONAL')
    elif s <= 15:
        print('VOTO NEGADO')
    elif (s > 17) and  (s <= 59):
        print('VOTO OBRIGATORIO')


print('-'*50)
print('...VOCE VOTA OU NÃO...')
print('-'*50)
num = int(input('Em que ano voce nasceu? '))

ano(num)