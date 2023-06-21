"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# num_str = input("Digite um  número inteiro: ")

# if num_str.isdigit():
#     num_int = int(num_str)
#     if num_int % 2 == 0:
#         print("Este número é par.")
#     else:
#         print("Este número é ímpar.")

# else:
#     print('Você não digitou um número inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# entrada_hora = input('Que horas são? (Ex: 02:30 / 18:45)')

# hora = entrada_hora[:2]

# if hora.isdigit():
#     hora_int = int(hora)

#     if (hora_int >= 0 and hora_int <= 11):
#         saudacao = "Bom dia!"
#         print(f'Olá {saudacao}')
#     elif (hora_int >= 12 and hora_int <= 17):
#         saudacao = "Boa Tarde!"
#         print(f'Olá {saudacao}')
#     else:
#         saudacao = "Boa Noite!"
#         print(f'Olá {saudacao}')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("Qual o seu nome?")
if nome:
    if len(nome) <= 4:
        print('Seu nome é curto')
    elif len(nome) >= 5 and len(nome) <= 6:
        print('Seu nome é normal.')
    elif len(nome) >= 7:
        print('Seu nome é muito grande.')
else:
    print('Digite alguma coisa')
