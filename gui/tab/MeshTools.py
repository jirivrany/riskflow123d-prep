# -*- coding: utf-8 -*-

'''
@author: Jiri Vrany

RiskFlow 123D
Tab widget for Mesh Tools
'''

from genui.tab.ui_mesh_tools import Ui_MeshTools
from PySide.QtGui import QWidget

from app import Settings

class MeshToolsTab(QWidget, Ui_MeshTools):
    '''
    Tab widget for Mesh Tools
    '''
    def __init__(self, parent = None):
        super(MeshToolsTab, self).__init__(parent)
        self.setupUi(self)
        
        #will be defined later from main window
        self.messenger = None
    
        