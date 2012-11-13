# -*- coding: utf-8 -*-

'''
@author: Jiri Vrany

Application Settings Tab
'''

from genui.tab.ui_material import Ui_material
from PySide.QtGui import QWidget, QFileDialog

from app import Settings

class MaterialTab(QWidget, Ui_material):
    '''
    Settings Tab Widget Matrial with generated UI
    '''
    def __init__(self, parent = None):
        super(MaterialTab, self).__init__(parent)
        self.setupUi(self)
        
        #will be defined later from main window
        self.messenger = None
    
        