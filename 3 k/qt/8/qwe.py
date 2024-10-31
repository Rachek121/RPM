import sys
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QFileDialog, QLabel, QLineEdit,    \
                                                                                         QVBoxLayout, QWidget
from collections import Counter
import re


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.textEdit = QTextEdit()
        self.setWindowIcon(QIcon('C:/Users/Proda/PycharmProjects/RPM/3 k/qt/8/logo.png'))
        self.openButton = QPushButton('Open')
        self.saveButton = QPushButton('Save')
        self.fileNameLineEdit = QLineEdit()

        self.charCountLabel = QLabel()
        self.wordCountLabel = QLabel()
        self.longestWordLabel = QLabel()
        self.shortestWordLabel = QLabel()
        self.mostCommonWordLabel = QLabel()

        self.openButton.clicked.connect(self.openFile)
        self.saveButton.clicked.connect(self.saveFile)
        self.textEdit.textChanged.connect(self.updateFileInfo)

        layout = QVBoxLayout()
        layout.addWidget(self.openButton)
        layout.addWidget(self.saveButton)
        layout.addWidget(self.fileNameLineEdit)
        layout.addWidget(self.textEdit)
        layout.addWidget(self.charCountLabel)
        layout.addWidget(self.wordCountLabel)
        layout.addWidget(self.longestWordLabel)
        layout.addWidget(self.shortestWordLabel)
        layout.addWidget(self.mostCommonWordLabel)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def openFile(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File")
        if filePath:
            with open(filePath, 'r') as file:
                text = file.read()
                self.textEdit.setPlainText(text)
                self.fileNameLineEdit.setText(filePath)

    def saveFile(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File")
        if filePath:
            with open(filePath, 'w') as file:
                file.write(self.textEdit.toPlainText())

    def updateFileInfo(self):
        text = self.textEdit.toPlainText()
        words = re.findall(r'\w+', text)
        word_count = len(words)
        char_count = len(text)
        word_counter = Counter(words)
        most_common_word = word_counter.most_common(1)[0][0] if word_counter else ''
        longest_word = max(words, key=len) if words else ''
        shortest_word = min(words, key=len) if words else ''

        self.charCountLabel.setText(f'Character count: {char_count}')
        self.wordCountLabel.setText(f'Word count: {word_count}')
        self.longestWordLabel.setText(f'Longest word: {longest_word}')
        self.shortestWordLabel.setText(f'Shortest word: {shortest_word}')
        self.mostCommonWordLabel.setText(f'Most common word: {most_common_word}')
# Edit by NoNSTOP Team (Rachek121)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
