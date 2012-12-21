# -*- coding: utf-8 -*-
'''
Created on 16.10.2012

@author: albert
'''

from PyQt4.QtGui import QMenuBar
from genui.ui_menu import Ui_menuBar


class MainMenu(QMenuBar, Ui_menuBar):
    '''
    Main Menu Class
    '''
    
    def __init__(self, parent = None):
        super(MainMenu, self).__init__(parent)
        self.setupUi(self)
        
        
    def disable_solver_actions(self):
        '''
        disable solver actions
        '''
        self.actionMonte_Carlo.setDisabled(True)
        self.actionBasic_Problem.setDisabled(True)
        self.actionSensitivy_task.setDisabled(True)
        
    def enable_solver_actions(self):
        '''
        enable actions when is safe
        '''
        self.actionMonte_Carlo.setEnabled(True)
        self.actionBasic_Problem.setEnabled(True)
        self.actionSensitivy_task.setEnabled(True)