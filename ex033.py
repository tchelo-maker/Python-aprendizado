a = int(input('primeiro valor '))
b = int(input('segundo numero '))
c = int(input('terceiro numero '))
#verificando quem é o menor
menor = a
if b<a and b<c:
     menor = b
if c<a and c<b:
    menor = c
#verificando quem é o maior
maior = a
if b>a and b>c:
     maior = a
if c>a and c>b:
    maior = c
print('o menor valor é {}'.format(menor))
print('maior valor é {} '.format(maior))