# from log import LogFileMixin, LogPrintMixin

# lp = LogPrintMixin()
# lp.log_error('Error')
# lp.log_sucess('Sucesso!!!')

# lf = LogFileMixin()
# lf.log_error('Error')
# lf.log_sucess('Sucesso!!!!')

from eletronico import Smartphone

galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('Iphone')

galaxy_s.ligar()
iphone.desligar()
