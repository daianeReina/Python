frase = 'O Python é uma linguagem de programação' \
    'multiparadigma'\
    'Python foi cvriado por Guido Van Rossun'

i = 0

qdte_letra_apareceu_mais = 0
letra_apareceu_mais = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == " ":
        i += 1
        continue

    qtde_letra_atual_aparece = frase.count(letra_atual)

    if qdte_letra_apareceu_mais < qtde_letra_atual_aparece:
        qdte_letra_apareceu_mais = qtde_letra_atual_aparece
        letra_apareceu_mais = letra_atual

    i += 1


print(
    f'A letra que apareceu mais foi "{letra_apareceu_mais}", essa letra apareceu {qdte_letra_apareceu_mais} vezes. ')
