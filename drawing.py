import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.flag = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            painter = QPainter()
            painter.begin(self)
            painter.setPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            painter.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            n = randint(2, 100)
            painter.drawEllipse(randint(0, 300), randint(0, 300), n, n)
            painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())