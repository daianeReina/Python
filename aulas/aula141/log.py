# Abstração
# Log

# Herança indica a relação de "É UM"

from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):  # esse trecho é chamado de assinatura do método
        raise NotImplementedError(
            'Implemente o método log'
        )

    # Ûma classe abstrata
    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):  # esse trecho é chamado de assinatura do método
        msg_formatada = f'{msg} => {self.__class__.__name__}'
        print('Salvando no log:', msg_formatada)
        with open(LOG_FILE, 'a') as file:
            file.write(msg_formatada)
            file.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):  # esse trecho é chamado de assinatura do método
        print(f'{msg} => {self.__class__.__name__} ')


if __name__ == '__main__':
    # l = Log()
    # l.log('Qualquer coisa') >>> não posso mais chamr esse método por causa do "_"(underscore)
    lp = LogPrintMixin()
    lp.log_error('Error')
    lp.log_sucess('Sucesso!!!')

    lf = LogFileMixin()
    lf.log_error('Error')
    lf.log_sucess('Sucesso!!!!')

    # print(LOG_FILE)
