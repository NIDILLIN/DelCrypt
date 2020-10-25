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

# import gui
import sys, os
sys.path.append('./Modules')

import ext_tools as fext

finder = fext.find_ext()

path = "/Modules/ext_tools.py"
file_path, extension = finder.split_filename_in(path)
print(finder._path)

print(extension)
print(file_path)

analyzer = fext.ext_analyzer()
analyzer.analyze(extension)












