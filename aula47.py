"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.


"""
import os

palavra_secreta = 'python'

letras_acertadas = ''

numero_tentativas = 0

while True:

    letra_digitada = input('Digite uma letra da palavra secreta: ')

    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas 1 letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            # print(letra_secreta)^
            palavra_formada += letra_secreta
        else:
            # print('*')
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!!!')
        print('A palavra era ', palavra_secreta)
        print('Tentativas: ', numero_tentativas)

        letras_acertadas = ''
        numero_tentativas = 0

    # for letra in palavra_secreta:

    #     if letra not in palavra_usuario:
    #         if letra == letra_digitada:
    #             palavra_usuario += letra_digitada

    #         else:
    #             palavra_usuario += '*'

    #     else:
    #         continue

    # print(palavra_usuario)
