# -*- coding: utf-8 -*-

'''
@author: Jiri Vrany

RiskFlow 123D
Tab widget for Mesh Tools
'''

from genui.tab.ui_montecarlo import Ui_MonteCarlo
from PySide.QtGui import QWidget

from app import Settings

class MonteCarloTab(QWidget, Ui_MonteCarlo):
    '''
    Tab widget for Mesh Tools
    '''
    def __init__(self, parent = None):
        super(MonteCarloTab, self).__init__(parent)
        self.setupUi(self)
        
        #will be defined later from main window
        self.messenger = None
    
        