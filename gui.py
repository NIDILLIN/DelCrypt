#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Copyright 2020 Nico Dillinger
#LICENSE
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

import sys
from PyQt5 import QApplication, QWidget


class dlcrypt(QWidget):
    def __init__(self):
        QWidget.__init__(self)


if __name__ == "__main__":
    app = QApplication([])
    window = dlcrypt()
    window.show()
    sys.exit(app.exec_())
