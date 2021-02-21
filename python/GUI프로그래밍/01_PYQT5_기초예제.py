from PyQt5.QtWidgets import *
import sys
from PyQt5 import uic

TestUI = r'C:\Users\스타트코딩\Desktop\main\python\python\GUI프로그래밍\01_PYQT5_기초예제.ui'

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(TestUI, self)

        self.pushButton.clicked.connect(self.showString) # 버튼을 눌렀을 때 showString 함수를 호출해라

    def showString(self):
        result = self.lineEdit.text()
        self.label.setText(result)

QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()

sys.exit(app.exec_())