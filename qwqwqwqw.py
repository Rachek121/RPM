import sys
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QImage, QPixmap, QColor, QTransform
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QSlider,
    QSpinBox,
    QComboBox,
    QFileDialog,
)


class ImageEditor(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Editor")

        # Изображение
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Слайдер прозрачности
        self.opacity_slider = QSlider(Qt.Orientation.Horizontal)
        self.opacity_slider.setRange(0, 255)
        self.opacity_slider.setValue(255)
        self.opacity_slider.valueChanged.connect(self.update_image)

        # SpinBox для поворота
        self.rotate_spinbox = QSpinBox()
        self.rotate_spinbox.setRange(0, 359)
        self.rotate_spinbox.setValue(0)
        self.rotate_spinbox.valueChanged.connect(self.update_image)

        # Комбобокс для выбора канала
        self.channel_combo = QComboBox()
        self.channel_combo.addItems(["Все каналы", "Красный", "Зеленый", "Синий"])
        self.channel_combo.currentIndexChanged.connect(self.update_image)

        # Кнопка открытия файла
        self.open_button = QPushButton("Открыть файл")
        self.open_button.clicked.connect(self.open_file)

        # Размещение элементов
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)

        control_layout = QHBoxLayout()
        control_layout.addWidget(self.open_button)
        control_layout.addWidget(self.rotate_spinbox)
        control_layout.addWidget(self.channel_combo)
        control_layout.addWidget(self.opacity_slider)
        layout.addLayout(control_layout)

        self.setLayout(layout)

        # Инициализация состояния
        self.image = None
        self.rotation = 0
        self.offset = QPoint(0, 0)  # Добавление смещения для перемещения

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Открыть изображение", "", "Изображения (*.png *.jpg *.jpeg)"
        )
        if file_name:
            try:
                self.image = QImage(file_name)
                if self.image.isNull():
                    raise Exception("Не удалось загрузить изображение")
                self.update_image()  # Обновляем изображение после успешной загрузки
            except Exception as e:
                print(f"Ошибка: {e}")

    def update_image(self):
        if self.image is None:
            return

        # Поворот изображения
        transform = QTransform()
        transform.rotate(self.rotate_spinbox.value())
        rotated_image = self.image.transformed(transform)

        # Изменение прозрачности
        opacity = self.opacity_slider.value() / 255
        rotated_image.setAlphaChannel(
            rotated_image.alphaChannel() * opacity
        )

        # Выбор цветового канала
        channel = self.channel_combo.currentIndex()
        if channel == 1:
            rotated_image = QImage(
                rotated_image.convertToFormat(QImage.Format.Format_Grayscale)
            )
        elif channel == 2:
            # Извлечение зеленого канала
            rotated_image = QImage(
                rotated_image.convertToFormat(QImage.Format.Format_Indexed8),
                rotated_image.width(),
                rotated_image.height(),
                QImage.Format.Format_Indexed8,
                rotated_image.constBits(),
                rotated_image.bytesPerLine(),
            )
            rotated_image.setColorTable(
                [QColor(0, 255, 0), QColor(0, 0, 0)]
            )
        elif channel == 3:
            # Извлечение синего канала
            rotated_image = QImage(
                rotated_image.convertToFormat(QImage.Format.Format_Indexed8),
                rotated_image.width(),
                rotated_image.height(),
                QImage.Format.Format_Indexed8,
                rotated_image.constBits(),
                rotated_image.bytesPerLine(),
            )
            rotated_image.setColorTable(
                [QColor(0, 0, 255), QColor(0, 0, 0)]
            )

        # Создание QPixmap с учетом смещения
        pixmap = QPixmap.fromImage(rotated_image)
        self.image_label.setPixmap(pixmap.copy(self.offset.x(), self.offset.y(), pixmap.width(), pixmap.height()))

        # Перемещение изображения в QLabel (не реализовано)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = ImageEditor()
    editor.show()
    sys.exit(app.exec())