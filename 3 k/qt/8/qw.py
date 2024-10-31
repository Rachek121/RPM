import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QSlider, QPushButton, QFileDialog
from PyQt6.QtGui import QPixmap, QImage, QColor, QTransform, QIcon
from PyQt6.QtCore import Qt


class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(1000, 1000)
        self.image_label = QLabel(self)
        self.setWindowTitle('NNST T')
        self.setWindowIcon(QIcon('C:/Users/Proda/PycharmProjects/RPM/3 k/qt/8/logo.png'))

        self.red_button = QPushButton('R', self)
        self.red_button.clicked.connect(lambda: self.change_color_channel('R'))

        self.green_button = QPushButton('G', self)
        self.green_button.clicked.connect(lambda: self.change_color_channel('G'))

        self.blue_button = QPushButton('B', self)
        self.blue_button.clicked.connect(lambda: self.change_color_channel('B'))

        self.all_channels_button = QPushButton('ALL', self)
        self.all_channels_button.clicked.connect(self.reset_color_channel)

        self.opacity_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.opacity_slider.setMinimum(0)
        self.opacity_slider.setMaximum(100)
        self.opacity_slider.setValue(100)
        self.opacity_slider.valueChanged.connect(self.change_opacity)

        self.rotate_left_button = QPushButton('Против часовой', self)
        self.rotate_left_button.clicked.connect(self.rotate_left)

        self.rotate_right_button = QPushButton('По часовой', self)
        self.rotate_right_button.clicked.connect(self.rotate_right)

        self.color_channel_button = QPushButton('Смена цвета', self)
        self.color_channel_button.clicked.connect(self.change_color_channel)

        self.open_button = QPushButton('Открыть изображение', self)
        self.open_button.clicked.connect(self.open_image)

        layout = QVBoxLayout(self)
        layout.addWidget(self.image_label)
        layout.addWidget(self.opacity_slider)
        layout.addWidget(self.rotate_left_button)
        layout.addWidget(self.rotate_right_button)
        layout.addWidget(self.color_channel_button)
        layout.addWidget(self.open_button)
        layout.addWidget(self.image_label)
        layout.addWidget(self.opacity_slider)
        layout.addWidget(self.rotate_left_button)
        layout.addWidget(self.rotate_right_button)
        layout.addWidget(self.red_button)
        layout.addWidget(self.green_button)
        layout.addWidget(self.blue_button)
        layout.addWidget(self.all_channels_button)
        layout.addWidget(self.open_button)

        self.setLayout(layout)

        self.pixmap = None
        self.angle = 0
        self.color_channel = 'Все'

    def open_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'За них или нас', '', 'NNST T (*.png *.xpm *.jpg *.bmp)')
        if file_path:
            self.pixmap = QPixmap(file_path)
            self.image_label.setPixmap(self.pixmap)

    def change_opacity(self):
        if self.pixmap:
            image = self.pixmap.toImage().convertToFormat(QImage.Format.Format_ARGB32)
            new_image = QImage(image.size(), QImage.Format.Format_ARGB32)
            for x in range(image.width()):
                for y in range(image.height()):
                    color = image.pixelColor(x, y)
                    new_color = QColor(color.red(), color.green(), color.blue(), self.opacity_slider.value())
                    new_image.setPixelColor(x, y, new_color)

            self.image_label.setPixmap(QPixmap.fromImage(new_image))

    def rotate_left(self):
        if self.pixmap:
            self.angle -= 90
            transform = QTransform().rotate(self.angle)
            self.image_label.setPixmap(self.pixmap.transformed(transform))

    def rotate_right(self):
        if self.pixmap:
            self.angle += 90
            transform = QTransform().rotate(self.angle)
            self.image_label.setPixmap(self.pixmap.transformed(transform))

    def change_color_channel(self, channel):
        if self.pixmap:
            image = self.pixmap.toImage()
            if image.format() == QImage.Format.Format_RGB32:
                new_image = QImage(image.size(), QImage.Format.Format_RGB32)
                for x in range(image.width()):
                    for y in range(image.height()):
                        color = image.pixelColor(x, y)
                        if channel == 'R':
                            new_image.setPixelColor(x, y, QColor(color.red(), 0, 0))
                        elif channel == 'G':
                            new_image.setPixelColor(x, y, QColor(0, color.green(), 0))
                        elif channel == 'B':
                            new_image.setPixelColor(x, y, QColor(0, 0, color.blue()))

                self.image_label.setPixmap(QPixmap.fromImage(new_image))
            else:
                self.image_label.setText("Изображение без цветов")

    def reset_color_channel(self):
        if self.pixmap:
            self.image_label.setPixmap(self.pixmap)

# Create by NoNSTOP Team(Rachek121)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec())