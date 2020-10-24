#-*-coding: utf-8-*-
import os

class find_ext():
	def split_and_find_ext_in(self, p):
		self._path = p
		self._path = os.path.(__file__)

		self._filename, self._file_ext = os.path.splitext(self._path)

		return self._filename, self._file_ext

class ext_analyzer(find_ext):
	if self._file_ext = ""



path = '/users/nidillin/Desktop/file_Name.ba6'

finder = find_ext()
finder.split(path) #returned file_Name & .ba6


.ba6
.a6
.b64
.sha

"""
import os

filename, file_extension = os.path.splitext('/path/to/somefile.ext')
that means split extension of file 

"""
