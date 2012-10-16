#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# copyright: Jiri Vrany <jiri.vrany@tul.cz>
# License GPL
'''

import sys
from PySide import QtGui

import gui.MainWindow

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)

	window = gui.MainWindow.MainWindow()
	window.show()

	sys.exit(app.exec_())

