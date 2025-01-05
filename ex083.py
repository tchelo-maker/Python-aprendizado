
ex = str(input('Digite uma expressão: '))
pilha = []
for simb in ex:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha)> 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expresão esta valida!')
else:
    print('Sua expressão esta invalida!')