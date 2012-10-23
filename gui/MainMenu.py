# -*- coding: utf-8 -*-
'''
Created on 16.10.2012

@author: albert
'''

from PySide.QtGui import QMenuBar
from genui.ui_menu import Ui_menuBar


class MainMenu(QMenuBar, Ui_menuBar):
    '''
    Main Menu Class
    '''
    
    def __init__(self, parent = None):
        super(MainMenu, self).__init__(parent)
        self.setupUi(self)