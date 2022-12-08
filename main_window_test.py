import os
import sys
from _iterator import Iterator
from _copy_rand import copy_to_random
from _copy import copy_to_another
from _writer_anno import write_annotation
from PyQt5 import QtWidgets, QtCore, QtGui
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
            "Copying to new directory with random number and create annotation", self
        )
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
        btn_bbear.clicked.connect(self.on_click_next_bbear)
        """
        self.lbl = QtWidgets.QLabel(self)
        self.pix = QtGui.QPixmap('icon.jpg')
        self.lbl.setPixmap(self.pix)
        self.lbl.resize(500, 500)
        self.lbl.move(200, 200)
        """
        self.show()

    def on_click_dataset(self) -> None:
        """
        Создаёт событие создания датасета
        """
        dataset_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder")
        if os.path.exists(dataset_path + "/brownbears") and os.path.exists(
            dataset_path + "/polarbears"
        ):
            path_csv = QtWidgets.QFileDialog.getExistingDirectory(
                self, "Select folder to save csvfile"
            )
            self.path_csv = write_annotation(dataset_path, path_csv)
            print(self.path_csv)

    def on_click_another(self) -> None:
        """
        Событие создания копирования
        """
        dataset_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder")
        if os.path.exists(dataset_path + "/brownbears") and os.path.exists(
            dataset_path + "/polarbears"
        ):
            path_another_dataset = QtWidgets.QFileDialog.getExistingDirectory(
                self, "Select folder to save another directory"
            )
            self.path_csv = copy_to_another(path_another_dataset, dataset_path)
            print(self.path_csv)

    def on_click_random(self) -> None:
        """
        Событие создания копирования с радномными номерами
        """
        dataset_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder")
        if os.path.exists(dataset_path + "/brownbears") and os.path.exists(
            dataset_path + "/polarbears"
        ):
            path_random_dataset = QtWidgets.QFileDialog.getExistingDirectory(
                self, "Select folder to save random directory"
            )
            self.path_csv = copy_to_random(dataset_path, path_random_dataset)
            print(self.path_csv)

    def on_click_next_pbear(self) -> None:
        """
        Событие переключения между картинками класса polarbears
        """
        if self.path_csv == "":
            msg = QMessageBox()
            msg.setWindowTitle("Message")
            msg.setText("There is no created annotation file yet")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
        else:
            iter = Iterator("polarbears", self.path_csv)
            while True:
                self.dialog = QMessageBox()
                self.dialog.addButton("Next bear", QMessageBox.AcceptRole)
                self.dialog.addButton("Stop", QMessageBox.RejectRole)
                self.dialog.setWindowTitle("Choose")
                self.dialog.setText("What's next?")
                self.dialog.exec()

                if self.dialog.clickedButton().text() == "Next bear":
                    image = iter.__next__()
                    self.image_window = ShowImage(image, self)
                    self.image_window.show()

                if self.dialog.clickedButton().text() == "Stop":
                    break

    def on_click_next_bbear(self) -> None:
        """
        Событие переключения между картинками класса brownbears
        """
        if self.path_csv == "":
            msg = QMessageBox()
            msg.setWindowTitle("Message")
            msg.setText("There is no created annotation file yet")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
        else:
            iter = Iterator("brownbears", self.path_csv)
            while True:
                self.dialog = QMessageBox()
                self.dialog.addButton("Next bear", QMessageBox.AcceptRole)
                self.dialog.addButton("Stop", QMessageBox.RejectRole)
                self.dialog.setWindowTitle("Choose")
                self.dialog.setText("What's next?")
                self.dialog.exec()

                if self.dialog.clickedButton().text() == "Next bear":
                    image = iter.__next__()
                    self.image_window = ShowImage(image, self)
                    self.image_window.show()

                if self.dialog.clickedButton().text() == "Stop":
                    break


class ShowImage(QtWidgets.QWidget):
    def __init__(self, path, parent=None) -> None:
        """
        Конструктор класса
        """
        super().__init__(parent, QtCore.Qt.Window)
        self.path_image = path
        self.viev()

    def viev(self) -> None:
        """
        Создаёт окно с картинкой
        """
        label = QLabel(self)
        pixmap = QPixmap(self.path_image)
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        self.move(600, 500)
        self.setWindowTitle("Bear")


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
