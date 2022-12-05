primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor == segundo_valor:
    print(f'{primeiro_valor=} é igual ao {segundo_valor=} ')

elif primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior do que o {segundo_valor=}')

elif primeiro_valor < segundo_valor:
    print(f'{primeiro_valor=} é menor do que o {segundo_valor=}')
