produtos = total = menor = cont = 0
barato = ' '
while True:
    print('====== LOJA ======')
    nome = str(input('PRODUTO: '))
    valor = float(input('valor do produto: '))
    escolha = str(input('quer continuar: s/n  ')).upper().strip()[0]
    if escolha not in 'Ss':
     break
    produtos += valor > 1000
    total += valor
    cont +=1
    if cont == 1:
        menor = valor
        barato = nome
    else:
        if valor < menor:
            menor = valor
            barato = nome
print('PAROU')
print('tem {} produtos que custa mais de R$1000 '.format(produtos))
print('total gasto foi {} '.format(total))
print('o produto mais barato é {} o valor dele é R${}'.format(barato,menor))