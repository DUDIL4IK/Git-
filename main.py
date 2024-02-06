import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('UI.ui', self)  # Загрузка интерфейса из файла UI.ui
        self.setWindowTitle('Генерация окружностей')

        self.pushButton.clicked.connect(self.add_circle)

        self.circles = []

    def add_circle(self):
        # Генерация случайных параметров для окружности
        x = random.randint(10, self.width() - 10)
        y = random.randint(10, self.height() - 10)
        diameter = random.randint(10, 100)

        # Добавление окружности в список для отрисовки
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for circle in self.circles:
            x, y, diameter = circle
            painter.setBrush(QColor(Qt.yellow))
            painter.drawEllipse(x - diameter / 2, y - diameter / 2, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())