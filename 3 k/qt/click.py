from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QApplication
from PyQt6.QtGui import QIcon
import sys


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(400, 400)
        self.setWindowTitle("Randomizer")
        self.setWindowIcon(QIcon("resourse/unnamed.ico"))
        layout = QVBoxLayout()
        layout.addStretch()
        self.label = QLabel("Случайное число: ")
        self.button = QPushButton("ням... нажми")
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addStretch()
        self.setLayout(layout)
        self.button.clicked.connect(self.generate_number)



    def generate_number(self):
        import random
        num_rn = random.randint(1, 1000)
        self.label.setText(f"Случайное число: {num_rn}")


def main():
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()