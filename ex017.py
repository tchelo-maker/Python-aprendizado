from math import hypot

catetoad= float(input('me fale o cateto adjacente de seu triangulo retangulo: '))
catetoop= float(input('me fale o cateto oposto: '))
hipo= hypot(catetoad, catetoop)
print('seu resultado deu {}'.format(hipo))
