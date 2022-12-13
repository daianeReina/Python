# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

correct_answers = 0

for question in perguntas:

    print('Pergunta:', question['Pergunta'])
    print()

    for number, option in enumerate(question['Opções']):
        print(f'{number})  {option}')
    
    print()
    
    answer = input('Escolha uma opção: ')

    correct_answer = False
    answer_integer = None
    total_options=len(question['Opções'])

    if answer.isdigit():
        answer_integer=int(answer)
    
    if answer_integer is not None:
        if answer_integer>=0 and answer_integer < total_options:
            if question['Opções'][answer_integer] == question['Resposta']:
                correct_answer = True

    print()

    if correct_answer:
        correct_answers += 1
        print('Acertou! 👍')
        
    else:
        print('Errou! ❌')

print(f'Você acertou {correct_answers} de {len(perguntas)} perguntas.')

# RESPOSTA DO PROFESSOR


# qtd_acertos = 0
# for pergunta in perguntas:
#     print('Pergunta:', pergunta['Pergunta'])
#     print()

#     opcoes = pergunta['Opções']
#     for i, opcao in enumerate(opcoes):
#         print(f'{i})', opcao)
#     print()

#     escolha = input('Escolha uma opção: ')

#     acertou = False
#     escolha_int = None
#     qtd_opcoes = len(opcoes)

#     if escolha.isdigit():
#         escolha_int = int(escolha)

#     if escolha_int is not None:
#         if escolha_int >= 0 and escolha_int < qtd_opcoes:
#             if opcoes[escolha_int] == pergunta['Resposta']:
#                 acertou = True

#     print()
#     if acertou:
#         qtd_acertos += 1
#         print('Acertou 👍')
#     else:
#         print('Errou ❌')

#     print()


# print('Você acertou', qtd_acertos)
# print('de', len(perguntas), 'perguntas.')


