# This Python file uses the following encoding: utf-8

import gui
import find_ext as fext 


finder = fext.find_ext()
path = os.path(__file__)

extension = finder.split_filename_and_find_ext_in(path)

analyzer = ext_analyzer()

analyzer.analyze(extension)
