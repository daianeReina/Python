# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('My Window')

button1 = QPushButton('Button1 Text')
# button.show()  # Adiciona o widget na hierarquia e exibe a janela
button1.setStyleSheet('font-size: 40px;')

button2 = QPushButton('Button2 Text')
# button2.show()  # Adiciona o widget na hierarquia e exibe a janela
button2.setStyleSheet('font-size: 40px;')

button3 = QPushButton('Button3 Text')
# button2.show()  # Adiciona o widget na hierarquia e exibe a janela
button3.setStyleSheet('font-size: 40px;')

layout = QGridLayout()

central_widget.setLayout(layout)

layout.addWidget(button1, 1, 1, 1, 1)
layout.addWidget(button2, 1, 2, 1, 1)
layout.addWidget(button3, 3, 1, 1, 2)

# status bar

status_bar = window.statusBar()
status_bar.showMessage('This is my status bar!')

# menubar


def slot_example(status_bar):
    status_bar.showMessage('O meu slot foi executado.')


menu = window.menuBar()
first_menu = menu.addMenu('Option_1')
first_action = first_menu.addAction('First Action')
first_action.triggered.connect(lambda: slot_example(status_bar))


window.show()
app.exec()  # O loop da aplicação
