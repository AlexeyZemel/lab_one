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

    