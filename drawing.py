import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from random import randint
from PyQt5 import uic


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Рисование')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.circle(qp)
        qp.end()

    def circle(self, qp):
        n = randint(2, 100)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(randint(0, 300), randint(0, 300), n, n)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())