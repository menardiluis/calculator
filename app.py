import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QPushButton, QGridLayout, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.setCentralWidget(self.cw)

        self.setWindowTitle('Calculadora do Luis')
        self.setFixedSize(400, 400)
        self.setStyleSheet('background: black;')

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            'background: black; color: white; font-size: 40px;'
        )
        self.display.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding)

        # Botões de números
        botao = 1
        for linha in range(1, 4):
            for coluna in range(0, 3):
                self.add_btn(QPushButton(str(botao)), linha, coluna, 1, 1)
                botao += 1
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)

        # Botões de operadores
        self.add_btn(QPushButton('.'), 4, 0, 1, 1)
        self.add_btn(QPushButton(''), 4, 2, 1, 1)
        self.add_btn(QPushButton('+'), 1, 3, 1, 1)
        self.add_btn(QPushButton('-'), 2, 3, 1, 1)
        self.add_btn(QPushButton('*'), 3, 3, 1, 1)
        self.add_btn(QPushButton('/'), 4, 3, 1, 1)
        self.add_btn(
            QPushButton('Del'), 1, 4, 1, 1, lambda: self.display.setText(
                self.display.text()[:-1]
            )
        )
        self.add_btn(
            QPushButton('C'), 2, 4, 1, 1, lambda: self.display.setText(''),
            'background: #ff3300; font-size: 18px;'
        )
        self.add_btn(
            QPushButton('='), 3, 4, 1, 1, self.eval_igual,
            'background: #66ff66; font-size: 18px;'
        )

        self.add_btn(QPushButton(''), 4, 4, 1, 1)

    # Class Function para adicionar botões
    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(funcao)
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        btn.setStyleSheet('font-size: 18px; background: gray; color: white;')
        if style:
            btn.setStyleSheet(style)

    # Class Function para definir '='
    def eval_igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception:
            self.display.setText('Conta inválida')


# Inicializador
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
