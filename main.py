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
import ext_tools as fext # ext analyzer
import crypto as cry # the main part, cryptography

# ===============================_GUI_================================
class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
	def __init__(self):
		# Это здесь нужно для доступа к переменным, методам
		super().__init__()
		self.setupUi(self)  # Это нужно для инициализации gui

		self.pushButton.clicked.connect(self.listWidget)
# ===============================_GUI_================================


# ========================_GUI_Initialization_========================
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

# if __name__ == '__main__':
#     main()  
main()
# ========================_GUI_Initialization_========================



# finder = fext.find_ext()
# analyzer = fext.ext_analyzer()

# path = "/Modules/ext_tools.py"
# extension = finder.split_filename_in(path)
# analyzer.analyze(extension)










