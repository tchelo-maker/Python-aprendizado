c = ('\033[m', # 0 - sem cores
     '\033[31m'  #1 - vermelho
     )


def ajuda(com):
    titulo(f'Acessando o manual comando \'{1}\'')
    help(com)

def titulo(msg, cor = 0):
    tam = len(msg) + 4
    print(c[cor],end='')
    print('~'*tam)
    print(f'  {msg} ')
    print('~'*tam)
    print(c[cor],end='')

#Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO')