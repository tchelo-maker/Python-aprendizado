nome = str(input('digite um nome. ')).strip()
ses = nome.split()
print('primeiro nome {} '.format(ses[0]))
print('ultimo nome {} '.format(ses[len(ses)-1]))