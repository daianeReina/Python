"""
Faça uma lista de comprar, com listas.
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com 
erros de índices inexistentes na sua lista 
"""

lista = []

while True:
    selecao = input(f'Selecione a opção [i]nserir [a]pagar [l]istar: ')

    if len(selecao) > 1:
        print('Digite apenas a letra inicial')

    if selecao.lower() == 'i':
        valor = input('Valor: ')
        lista.append(valor)

    elif selecao.lower() == 'a':

        indice_digitado = input('Qual índice deseja apagar?')

        if len(lista) > 0:
            try:
                num_indice = int(indice_digitado)
                print(
                        f'O item "{lista[num_indice]}" foi deletado da sua lista.')
                lista.pop(num_indice)

            except ValueError:
                print('Digite um número inteiro.')

            except IndexError:
                print('Índice não existe na lista.')


        else:
            print('Lista vazia, não há nada para apagar.')

    elif selecao.lower() == 'l':
        if len(lista) == 0:
            print('Lista vazia.')

        for indice, nome in enumerate(lista):
            print(indice, nome)

    else:
        print('Digite uma seleção válida.')
