#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2020 Nico Dillinger
# LICENSE
"""
This file is part of DelCrypt.
DelCrypt is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

DelCrypt is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with DelCrypt.  If not, see <https://www.gnu.org/licenses/>.
"""
import sys, os
sys.path.append('./Modules')
sys.path.append('./UI')

from PyQt5 import QtWidgets

import design # ui
import ext_tools as fext # extension analyzer
import crypto as cry # cryptography

# ===============================_GUI_================================
class gui(QtWidgets.QMainWindow, design.Ui_MainWindow):
	def __init__(self):
		super().__init__() 

		self.setupUi(self)  # gui init
		self.pushButton.clicked.connect(self.encryptThis)


	def encryptThis (self):
		item = self.lineEdit.text()
		passcode = self.lineEdit_2.text()

		encryptedText = cry.encrypt(item, passcode)

		self.listWidget.addItem(encryptedText)
# ===============================_GUI_================================


# ========================_GUI_Initialization_========================
def main():
    app = QtWidgets.QApplication(sys.argv)  # QApplication
    window = gui()  # Making window object gui`s class
    window.show()  # Show window
    app.exec_()  # app run

if __name__ == '__main__':
    main()  
# ========================_GUI_Initialization_========================



# finder = fext.find_ext()
# analyzer = fext.ext_analyzer()

# path = "/Modules/ext_tools.py"
# extension = finder.split_filename_in(path)
# analyzer.analyze(extension)