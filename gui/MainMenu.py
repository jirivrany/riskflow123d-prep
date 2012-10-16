# -*- coding: utf-8 -*-
'''
Created on 16.10.2012

@author: albert
'''

from genui.ui_menu import Ui_menuBar
from PySide import QtGui


class MainMenu(QtGui.QMenuBar, Ui_menuBar):
    
    def __init__(self, parent = None):
        super(MainMenu, self).__init__(parent)
        self.setupUi(self)
        
