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

import design
import ext_tools as fext
import crypto as cry


# ===================================================================
class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
	def __init__(self):
		# Это здесь нужно для доступа к переменным, методам
		super().__init__()
		self.setupUi(self)  # Это нужно для инициализации gui

		self.pushButton.clicked.connect(self.lineEdit.clear)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

# if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
#     main()  # то запускаем функцию main()

main()
# ===================================================================


"""
finder = fext.find_ext()
analyzer = fext.ext_analyzer()

path = "/Modules/ext_tools.py"
extension = finder.split_filename_in(path)
# analyzer.analyze(extension)

this = os.urandom(32) # абстрактный файл для шифровки

cry.encrypt(this) # encrypt this and print output
cry.decrypt(this) # decrypt this and print output
"""









