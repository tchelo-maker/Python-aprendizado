sexo = str(input('Informe seu sexo: m/f   ')).strip().upper()[0]
while sexo not in 'MF':
     sexo = str(input('dados invalidos por favor informe seu sexo: ')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(sexo))

