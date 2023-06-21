import abc  # import the abstract method


class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float:
        ...

    def depositar(self, valor: float):
        self.saldo += valor
        self.detalhes(f'DEPÓSITO DE R${valor}.')
        return self.saldo

    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo atual é de R${self.saldo:.2f} {msg}')
        print('--')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def sacar(self, valor: float):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'SAQUE DE R${valor:.2f}.')
            return self.saldo

        print('Não foi possível sacar o valor desejado.')
        self.detalhes(f'(SAQUE NEGADO DE R${valor:.2f})')


class ContaCorrente(Conta):

    def __init__(self, agencia: int, conta: int, saldo: float = 0, limite: float = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'SAQUE DE R${valor:.2f}.')
            return self.saldo

        print('Não foi possível sacar o valor desejado.')
        print(f'Seu limite é de R${- self.limite:.2f}.')
        self.detalhes(f'(SAQUE NEGADO DE R${valor:.2f})')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r})'
        return f'{class_name}{attrs}'


# Essa condicional abaixo é para que o meu código dentro da condicional
# seja executado apenas no arquivo de origem.:)

if __name__ == '__main__':
    # cont_poup_1 = ContaPoupanca(111, 222)
    # cont_poup_1.sacar(1)
    # cont_poup_1.depositar(1)
    # cont_poup_1.sacar(1)
    # cont_poup_1.sacar(1)
    # print('###########')

    cont_corr_1 = ContaCorrente(111, 222, 0, 100)
    cont_corr_1.sacar(1)
    cont_corr_1.depositar(1)
    cont_corr_1.sacar(1)
    cont_corr_1.sacar(110)

    print('###########')
