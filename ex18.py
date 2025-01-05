import math

angulo = float(input('me de um angulo '))
seno = math.cos(math.radians(angulo))
coseno = math.sin(math.radians(angulo))
tangent = math.tan(math.radians(angulo))
print(' o seno desse angulo é {:.2f} o coseno é {:.2f} e o tangent é {:.2f}'.format(seno,coseno,tangent))
