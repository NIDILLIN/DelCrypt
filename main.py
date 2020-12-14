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
sys.path.append('./Languages')
sys.path.append('./Modules')
sys.path.append('./UI')

from PyQt5 import QtWidgets

lang = 'russian'
if lang == 'russian':
    import rus as lang
else:
    import eng as lang

import design # ui
import ext_tools as fext # extension analyzer, spliting exts
import crypto as cry # cryptography

# ========================--Crypto-class--=========================
class crypto():
	def encrypt(self, item, passcode):
		item = item
		passcode = passcode

		encryptedText = cry.encrypt(item, passcode)
		return encryptedText

	def decrypt(self, item, passcode):
		item = item
		passcode = passcode

		decryptedText = cry.decrypt(item, passcode)
		return decryptedText
# ========================--Crypto-class--=========================

# ============================--GUI--==============================
class gui(QtWidgets.QMainWindow, design.Ui_MainWindow, crypto):
	def __init__(self):
		super().__init__() 

		self.setupUi(self)  # gui init
		self.setWindowTitle('DelCrypt')
		self.pushButton.clicked.connect(self.encryptThis)
		self.pushButton_2.clicked.connect(self.decryptThis)

	def error (self, message):	# error function for err_msg
		self.err = QtWidgets.QErrorMessage()
		self.err.showMessage(message)


	def areTwoLinesEmpty(self, line1, line2):
		if line1 == '':
			self.line1_isEmpty = True
		else:
			self.line1_isEmpty = False
		if line2 == '':
			self.line2_isEmpty = True
		else:
			self.line2_isEmpty = False

		return self.line1_isEmpty, self.line2_isEmpty


	def encryptThis(self):
		self.areTwoLinesEmpty(self.lineEdit.text(), self.lineEdit_2.text()) # if empty -- true

		if self.line1_isEmpty:
			self.error(lang.dic['error-textLineIsEmpty'])
		elif self.line2_isEmpty:
			self.error(lang.dic['error-passLineIsEmpty'])
		else:
			encryptedText = self.encrypt(self.lineEdit.text(), self.lineEdit_2.text())
			self.listWidget.addItem(encryptedText)

	def decryptThis(self):
		self.areTwoLinesEmpty(self.lineEdit.text(), self.lineEdit_2.text()) # if empty -- true
		try:
			if self.line1_isEmpty:
				self.error(lang.dic['error-textLineIsEmpty'])
			elif self.line2_isEmpty:
				self.error(lang.dic['error-passLineIsEmpty'])
			else:
				decryptedText = self.decrypt(self.lineEdit.text(), self.lineEdit_2.text())
				self.listWidget.addItem(decryptedText)

		except:
			self.error(lang.dic['error-uncorrectPasscode'])
		
		
# ============================--GUI--==============================


# ====================--GUI_Initialization--=======================
def main():
    app = QtWidgets.QApplication(sys.argv)  # QApplication
    window = gui()  # Making window object gui`s class
    window.show()  # Show window
    app.exec_()  # app run

if __name__ == '__main__':
    main()  
# ====================--GUI_Initialization--=======================



# finder = fext.find_ext()
# analyzer = fext.ext_analyzer()

# path = "/Modules/ext_tools.py"
# extension = finder.split_filename_in(path)
# analyzer.analyze(extension)