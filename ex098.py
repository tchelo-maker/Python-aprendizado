
from time import sleep
def linha():
    print('='*30)
def contador(i, f , p):
        linha()
        print(f'Contagem de {i} ate {f} de {p} em {p}')
        sleep(0.5)
        if p < 0:
            p *= -1
        if p == 0:
            p = 1
        if i < f:
            cont = i
            while cont <= f:
                print(f'{cont} ', end='' , flush=True)
                sleep(0.5)
                cont += p
            print('FIM')
        else:
            cont = i
            while cont >= f:
                print(f'{cont} ', end='', flush=True)
                sleep(0.5)
                cont -= p
            print('FIM')

contador(1 , 10 , 1)
contador(10,0,2)
linha()
print('Agora é sua vez de fazer a contagem')
ini= int(input('Inicio: '))
mei=int(input('Meio:    '))
pas=int(input('pas :    '))
contador(ini, mei , pas)


