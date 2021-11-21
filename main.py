import sys
import random
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QPolygon, QPen
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджета
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


# Унаследуем наш класс от простейшего графического примитива QWidget
class SimplePlanner(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.setWindowTitle("Минипланировщик")
        self.events = True
        self.pushButton.clicked.connect(self.check)

    def check(self):
        self.update()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:

        x, y = random.randint(0, 800), random.randint(0, 580)
        Qpainter = QPainter()
        Qpainter.begin(self)
        Qpainter.setBrush(QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        radius = random.randint(10, 100)
        Qpainter.drawEllipse(x, y, radius, radius)
        Qpainter.end()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimplePlanner()
    ex.show()
    sys.exit(app.exec())
