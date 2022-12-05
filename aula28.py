"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

if len(nome) == 0 or len(idade) == 0:
    print("Sorry, you need to  put your name and you age ")

else:
    print(f'Your name is {nome}.')
    print(f'Your inverted name is {nome[::-1]}')

    if ' ' in nome:
        print('Your name have spaces.')
    else:
        print("Your name doesn't have spaces.")

    print(f'Your name has {len(nome)} letters.')
    print(f'The first letter of your name is "{nome[0]}".')
    print(f'The last letter of your name is "{nome[-1]}".')
