# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)
class MyError(Exception):
    ...


class OtherError(Exception):
    ...


def levantar():
    exception_ = MyError('a', 'b', 'c')  # qdo uso raise nunca retorna
    exception_.add_note('Olha a nota 1')  # Adicionando notas aos erros.
    exception_.add_note('Vc errou isso.')
    raise exception_

# Como tratar a exceção:


try:
    levantar()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()

    # relançando a exceção #

    exception_ = OtherError('Vou lançar de novo.')
    exception_.add_note('Mais uma nota.')
    exception_.__notes__ += error.__notes__.copy()

    raise exception_
