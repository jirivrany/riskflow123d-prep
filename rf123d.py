#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# copyright: Jiri Vrany <jiri.vrany@tul.cz>
# Technical University of Liberec
# New Technology Institute
'''

import sys
from PyQt4 import QtGui


import gui.MainWindow


def main():
    '''
    main application loop
    '''
    app = QtGui.QApplication(sys.argv)
    window = gui.MainWindow.MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
