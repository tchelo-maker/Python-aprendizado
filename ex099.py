from time import sleep
def linha():
    print('='*50)
def maior(*num):
    print()
    linha()
    print('ANALISANDO OS VALORES PASSADOS...')
    for valor in num:
        sleep(0.5)
        print(f'{valor} ',end='')
    print(f'Foram informado {len(num)}  valores ao todo')
    print(f'O maior valor é {max(num)}')












maior(1,2,3,4,5,6)
maior(7,8,9,0)
maior(9,7,21,2,3)