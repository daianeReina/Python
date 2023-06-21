import contas

import pessoas


class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[pessoas.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None,
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            return True
        return False

    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('_checa_se_conta_e_do_cliente', False)
        return False

    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self._checa_agencia(conta) and self._checa_cliente(conta) and self._checa_conta(conta) and self._checa_se_conta_e_do_cliente(cliente, conta)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':

    cliente_1 = pessoas.Cliente('Daiane', 30)
    cliente_1_CC = contas.ContaCorrente(111, 222, 0, 0)
    cliente_1.conta = cliente_1_CC

    cliente_2 = pessoas.Cliente('Maria', 18)
    cliente_2_CP = contas.ContaPoupanca(111, 222)
    cliente_2.conta = cliente_2_CP
    banco = Banco()

    banco.clientes.extend([cliente_1, cliente_2])
    banco.contas.extend([cliente_1_CC, cliente_2_CP])
    banco.agencias.extend([111, 222])

    if banco.autenticar(cliente_1, cliente_1_CC):
        cliente_1_CC.depositar(10)
        cliente_1.conta.depositar(100)
        print(cliente_1.conta)
