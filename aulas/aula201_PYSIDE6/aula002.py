# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QGridLayout, QWidget

app = QApplication(sys.argv)

button = QPushButton('Button Text')
# button.show()  # Adiciona o widget na hierarquia e exibe a janela
button.setStyleSheet('font-size: 40px;')

button2 = QPushButton('Button2 Text')
# button2.show()  # Adiciona o widget na hierarquia e exibe a janela
button2.setStyleSheet('font-size: 40px;')

button3 = QPushButton('Button3 Text')
# button2.show()  # Adiciona o widget na hierarquia e exibe a janela
button3.setStyleSheet('font-size: 40px;')

central_widget = QWidget()
layout = QGridLayout()

central_widget.setLayout(layout)

layout.addWidget(button, 1, 1, 1, 1)
layout.addWidget(button2, 1, 2, 1, 1)
layout.addWidget(button3, 3, 1, 1, 2)

central_widget.show()  # Adiciona o central_widget na hierarquia e exibe a janela
app.exec()  # O loop da aplicação
