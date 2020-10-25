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

import os


class find_ext():
	def split_filename_in(self, p):
		self._path = p
		self._filename, self._file_ext = os.path.splitext(self._path)

		return self._filename, self._file_ext

class ext_analyzer(find_ext):
	def analyze(self, object):
		self.file_ext = object

		if self.file_ext == ".b64": #just base64
			print("It`s .b64")
		elif self.file_ext == ".ba6": #base64 + aes256
			print("It`s .ba6")
		elif self.file_ext == ".ba8": #base64 + aes128
			print("It`s .ba8")
		elif self.file_ext == ".py":
			print("It`s .py")
		else: print("Something wrong in *ext_tools** module, at *ext_analyzer* method")

