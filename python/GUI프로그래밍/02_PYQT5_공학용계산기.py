from PyQt5.QtWidgets import *
import sys
from PyQt5 import uic
import math

TestUI = r'C:\Users\스타트코딩\Desktop\main\python\python\GUI프로그래밍\02_PYQT5_공학용계산기.ui'

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(TestUI, self)

        self.pushButton.clicked.connect(self.calculate)

    def calculate(self):
        foo = self.lineEdit.text()
        result = eval(foo)
        result_for_history = f"{foo}\n={result}\n"
        self.history.append(str(result_for_history))
        self.lineEdit.clear()

QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()

sys.exit(app.exec_())