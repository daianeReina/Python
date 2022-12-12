# Exercícios com funções


# 1

def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


resultado_final = multiplicacao(2, 2, 2, 2, 2)
print(f'Resultado da Multiplicação: {resultado_final}')

# 2

while True:
    try:

        def par_ou_impar(numero):
            if (int(numero) % 2) == 0:
                return (f'O número "{numero}" é PAR.')
            return f'O número "{numero}" é ÍMPAR.'

        resultado_final= par_ou_impar(input('Digite um número: '))
        print(resultado_final)
    except ValueError:
        print('Digite um número inteiro.')


