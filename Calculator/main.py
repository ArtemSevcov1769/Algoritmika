from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QGridLayout, QPushButton)
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLineEdit, QSizePolicy

class Display(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

class StretchButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(50, 50)
        self.setStyleSheet('''
            QPushButton {
            background-color: #000000;
            color: #ffffff;
            border-radius: 15px;
            }
        ''')

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Калькулятор')
        self.setGeometry(0, 0, 350, 500)
        self.create_grid_layout()
        self.to_slove = ''
        self.setStyleSheet('''
        QWidget{
        background-color: #d7d7d7;
            }
        ''')
    def create_grid_layout(self):
        layout = QGridLayout()
        btn_1 = StretchButton('1')
        btn_2 = StretchButton('2')
        btn_3 = StretchButton('3')
        btn_4 = StretchButton('4')
        btn_5 = StretchButton('5')
        btn_6 = StretchButton('6')
        btn_7 = StretchButton('7')
        btn_8 = StretchButton('8')
        btn_9 = StretchButton('9')
        btn_0 = StretchButton('0')
        btn_plus = StretchButton('+')
        btn_minus = StretchButton('-')
        btn_ravno = StretchButton('=')
        btn_umn = StretchButton('*')
        btn_del = StretchButton('/')
        self.edit = Display()
        btn_pount = StretchButton('.')
        btn_clear = StretchButton('c')
        btn_delit = StretchButton('<-')
        btn_1.clicked.connect(self.btn_handler)
        btn_2.clicked.connect(self.btn_handler)
        btn_3.clicked.connect(self.btn_handler)
        btn_4.clicked.connect(self.btn_handler)
        btn_5.clicked.connect(self.btn_handler)
        btn_6.clicked.connect(self.btn_handler)
        btn_7.clicked.connect(self.btn_handler)
        btn_8.clicked.connect(self.btn_handler)
        btn_9.clicked.connect(self.btn_handler)
        btn_0.clicked.connect(self.btn_handler)
        btn_plus.clicked.connect(self.btn_handler)
        btn_umn.clicked.connect(self.btn_handler)
        btn_minus.clicked.connect(self.btn_handler)
        btn_ravno.clicked.connect(self.btn_handler)
        btn_del.clicked.connect(self.btn_handler)
        btn_delit.clicked.connect(self.btn_handler)
        btn_pount.clicked.connect(self.btn_handler)


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
        layout.addWidget(self.edit, 0, 0, 1, 4)
        layout.addWidget(btn_pount, 5, 2)
        layout.addWidget(btn_delit, 1, 0)
        layout.addWidget(btn_clear, 1, 1)
        self.setLayout(layout)
    def btn_handler(self):
        btn = self.sender()
        if btn.text() in '0123456789+-*/.':
            self.to_slove += btn.text()
        if btn.text() == '<-':
            self.to_slove = self.to_slove[0:-1]
        if btn.text() == 'c':
            self.to_slove = ''
        if btn.text() == '=':
            self.to_slove = str(eval(self.to_slove))
        self.edit.setText(self.to_slove)


if __name__ == '__main__':
    app = QApplication([])
    win = MainWindow()
    win.show()
    app.exec_()