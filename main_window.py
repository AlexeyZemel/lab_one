import os
import sys
from _iterator import Iterator
from _copy_rand import copy_to_random
from _copy import copy_to_another
from _writer_anno import write_annotation
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MainWindow(QWidget):
    def __init__(self) -> None:
        """
        Инициализирует объект класса
        """
        super().__init__()
        self.initUI()
        self.path_csv = ""

    def initUI(self) -> None:
        """
        Создание GUI
        """
        QToolTip.setFont(QFont("SansSerif", 7))

        self.setGeometry(500, 500, 500, 420)
        self.setWindowTitle("Bears")
        self.setWindowIcon(QIcon("icon.jpg"))

        btn_first = QPushButton("Create annotation from dataset", self)
        btn_first.setToolTip("<i>Create</i>")
        btn_first.resize(btn_first.sizeHint())
        btn_first.move(50, 50)
        btn_first.clicked.connect(self.on_click_dataset)

        btn_second = QPushButton(
            "Copying to another directory and create annotation", self
        )
        btn_second.setToolTip("<i>Copy</i>")
        btn_second.resize(btn_second.sizeHint())
        btn_second.move(50, 100)
        btn_second.clicked.connect(self.on_click_another)

        btn_third = QPushButton(
            "Copying to new directory with random number and create annotation", self)
        btn_third.setToolTip("<i>Copy with random number</i>")
        btn_third.resize(btn_third.sizeHint())
        btn_third.move(50, 150)
        btn_third.clicked.connect(self.on_click_random)

        btn_pbear = QPushButton("Polar bear", self)
        btn_pbear.setToolTip("<i>Shows the polar bear</i>")
        btn_pbear.resize(btn_pbear.sizeHint())
        btn_pbear.move(50, 200)
        btn_pbear.clicked.connect(self.on_click_next_pbear)

        btn_bbear = QPushButton("Brown bear", self)
        btn_bbear.setToolTip("<i>Shows the brown bear</i>")
        btn_bbear.resize(btn_bbear.sizeHint())
        btn_bbear.move(50, 250)
        btn_bbear.clicked.connect(self.on_click_next_pbear)

        self.show()

    def on_click_dataset(self) -> None:
        """
        Создаёт событие создания датасета
        """
        dataset_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder")
        if os.path.exists(dataset_path + "/brownbears") and os.path.exists(
            dataset_path + "/polarbears"
        ):
            path_csvfile_dataset = QtWidgets.QFileDialog.getExistingDirectory(
                self, "Select folder to save csvfile"
            )
            self.path_csv = write_annotation(dataset_path, path_csvfile_dataset)
            print(self.path_csv)

    def on_click_another(self):
        dataset_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder")
        if os.path.exists(dataset_path + "/brownbears") and os.path.exists(
            dataset_path + "/polarbears"
        ):
            path_another_dataset = QtWidgets.QFileDialog.getExistingDirectory(
                self, "Select folder to save another directory"
            )
            self.path_csv = copy_to_another(dataset_path, path_another_dataset)
            print(self.path_csv)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
