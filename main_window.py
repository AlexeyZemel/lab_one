import os
import sys
from _iterator import Iterator
from _copy_rand import copy_to_random
from _copy import copy_to_another
from _writer_anno import write_annotation
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
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
        self.setGeometry(500, 500, 900, 420)
        self.setWindowTitle("Bears")
        self.setWindowIcon(QIcon("icon.jpg"))

        pix = QPixmap('icon.jpg')
        item = QGraphicsPixmapItem(pix)
        scene = QGraphicsScene(self)
        scene.addItem(item)
        view = QGraphicsView(scene)
        self.setCentralWidget(view)

        menubar = self.menuBar()
        first = menubar.addMenu("Create annotation dataset")
        action1 = QAction("Create", self)
        action1.triggered.connect(self.on_click_dataset)
        first.addAction(action1)

        second = menubar.addMenu("Copying to another directory")
        action2 = QAction("Copying", self)
        action2.triggered.connect(self.on_click_another)
        second.addAction(action2)

        third = menubar.addMenu("Copying to new directory with random number")
        action3 = QAction("Copying with random number", self)
        action3.triggered.connect(self.on_click_random)
        third.addAction(action3)

        fourth = menubar.addMenu("Polar bear")
        action4 = QAction("Show Polar bear", self)
        action4.triggered.connect(self.on_click_next_pbear)
        fourth.addAction(action4)

        fifth = menubar.addMenu("Brown bear")
        action5 = QAction("Show Brown bear", self)
        action5.triggered.connect(self.on_click_next_bbear)
        fifth.addAction(action5)

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
        if os.path.exists(dataset_path + "/cat") and os.path.exists(
            dataset_path + "/dog"
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
                    pix = QPixmap(image)
                    item = QGraphicsPixmapItem(pix)
                    scene = QGraphicsScene(self)
                    scene.addItem(item)
                    view = QGraphicsView(scene)
                    self.setCentralWidget(view)

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
                    pix = QPixmap(image)
                    item = QGraphicsPixmapItem(pix)
                    scene = QGraphicsScene(self)
                    scene.addItem(item)
                    view = QGraphicsView(scene)
                    self.setCentralWidget(view)

                if self.dialog.clickedButton().text() == "Stop":
                    break


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
    