# -*- coding: utf-8 -*-

'''
@author: Jiri Vrany

Application Settings Tab
'''

from genui.tab.ui_mesh_settings import Ui_MeshSettings
from PySide.QtGui import QWidget

from app import Settings

class MeshSettingsTab(QWidget, Ui_MeshSettings):
    '''
    Tab widget for Mesh Settings
    '''
    def __init__(self, parent = None):
        super(MeshSettingsTab, self).__init__(parent)
        self.setupUi(self)
        
        #will be defined later from main window
        self.messenger = None
    
        