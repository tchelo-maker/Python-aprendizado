num = int(input('digite um numero! '))
print('qual sera sua base de conversão \n 1-binario \n 2-octal \n 3-hexadecimal.')
decisao = int(input('escolha qual: '))
if decisao == 1:
    print('convertendo fica {}'.format(bin(num)))
elif decisao == 2:
    print('convertendo patra octal {} '.format(oct(num)))
elif decisao == 3:
    print('convertendo para {} hexadecimal'.format(hex(num)))

