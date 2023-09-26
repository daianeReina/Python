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

from PySide6.QtCore import Slot
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


@Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage('O meu slot foi executado.')
    return inner


@Slot()
def slot_example2(checked):
    print('Está marcado?', checked)


@Slot()
def slot_exemple3(action):
    def ineer():
        slot_example2(action.isChecked())
    return ineer


menu = window.menuBar()
first_menu = menu.addMenu('Option_1')
first_action = first_menu.addAction('First Action')
first_action.triggered.connect(slot_example(status_bar))

second_action = first_menu.addAction('Second Action')
second_action.setCheckable(True)
second_action.toggled.connect(slot_example2)
second_action.hovered.connect(slot_exemple3(second_action))

button1.clicked.connect(slot_exemple3(second_action))


window.show()
app.exec()  # O loop da aplicação
