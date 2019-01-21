import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

app = QApplication(sys.argv)
w = QWidget()
w.resize(250, 150)
w.move(300, 300)
w.setWindowTitle('Simple')
w.show()

sys.exit(app.exec_())

