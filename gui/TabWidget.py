# -*- coding: utf-8 -*-

from genui.ui_tabwidget import Ui_TabWidget
from PySide import QtGui

from gui.tab.FlowCheck import FlowCheck

TAB_LABELS = {
              'flow' : u'Flow ini editor',
              
              }

class MainTabWidget(QtGui.QTabWidget, Ui_TabWidget):
    
    def __init__(self, parent = None):
        super(MainTabWidget, self).__init__(parent)
        self.setupUi(self)
        
        self.tab_flow_ini = FlowCheck()
        self.addTab(self.tab_flow_ini, TAB_LABELS['flow'])

