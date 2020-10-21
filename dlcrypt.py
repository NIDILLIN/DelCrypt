# This Python file uses the following encoding: utf-8
import sys
from PyQt import QApplication, QWidget


class dlcrypt(QWidget):
    def __init__(self):
        QWidget.__init__(self)


if __name__ == "__main__":
    app = QApplication([])
    window = dlcrypt()
    window.show()
    sys.exit(app.exec_())
