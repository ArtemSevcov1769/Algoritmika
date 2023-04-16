from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QGridLayout, QPushButton)
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Калькулятор')
        self.setGeometry(0, 0, 350, 500)
        self.create_grid_layout()

    def create_grid_layout(self):
        layout = QGridLayout()
        btn_1 = QPushButton('1')
        btn_2 = QPushButton('2')
        btn_3 = QPushButton('3')
        btn_4 = QPushButton('4')
        btn_5 = QPushButton('5')
        btn_6 = QPushButton('6')
        btn_7 = QPushButton('7')
        btn_8 = QPushButton('8')
        btn_9 = QPushButton('9')
        btn_0 = QPushButton('0')
        btn_plus = QPushButton('+')
        btn_minus = QPushButton('-')
        btn_ravno = QPushButton('=')
        btn_umn = QPushButton('x')
        btn_del = QPushButton(':')

        layout.addWidget(btn_1, 4, 0)
        layout.addWidget(btn_2, 4, 1)
        layout.addWidget(btn_3, 4, 2)
        layout.addWidget(btn_4, 3, 0)
        layout.addWidget(btn_5, 3, 1)
        layout.addWidget(btn_6, 3, 2)
        layout.addWidget(btn_7, 2, 0)
        layout.addWidget(btn_8, 2, 1)
        layout.addWidget(btn_9, 2, 2)
        layout.addWidget(btn_0, 5, 0, 1, 2)
        layout.addWidget(btn_plus, 1, 2)
        layout.addWidget(btn_ravno, 4, 3, 2, 1)
        layout.addWidget(btn_del, 3, 3)
        layout.addWidget(btn_umn, 2, 3)
        layout.addWidget(btn_minus, 1, 3)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
