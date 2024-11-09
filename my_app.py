from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from second_win import *
from inst import *

'''txt_title = 'Health'
win_x, win_y = 200, 100
win_width, win_height = 1000, 600'''

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear() #aparencia da janela
        self.initUI() #criar e configurar elementos graficos
        self.connects() #estabelece conexoes entre alementos
        self.show() #iniciar
        
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        
    def initUI(self):
        self.hello = QLabel(txt_hello) #cria uma etiqueta
        self.instruction= QLabel(txt_instruction) #cria uma etiqueta
        self.button = QPushButton(txt_next) # cria uma botao
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.button, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)
    
    def connects(self):
        self.button.clicked.connect(self.next_click)
        self.hide()
        self.tw = TestWin()
    
app = QApplication([])
mw = MainWin()
app.exec()