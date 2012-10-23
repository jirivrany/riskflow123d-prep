# -*- coding: utf-8 -*-

from genui.ui_tabwidget import Ui_TabWidget
from PySide import QtGui

from gui.tab.FlowCheck import FlowCheck
from gui.tab.Settings import SettingsTab

from gui.Communicate import Communicate

TAB_LABELS = {
              'flow' : u'Flow ini editor',
              'settings' : u'Settings',
              }

class MainTabWidget(QtGui.QTabWidget, Ui_TabWidget):
    
    def __init__(self, parent = None):
        super(MainTabWidget, self).__init__(parent)
        self.setupUi(self)
        
        self.tab_flow_ini = FlowCheck()
        self.addTab(self.tab_flow_ini, TAB_LABELS['flow'])
        
        self.tab_settings = SettingsTab()
        self.addTab(self.tab_settings, TAB_LABELS['settings'])
        
        self.messenger = Communicate()
        
        self.tab_flow_ini.messenger = self.messenger
        self.tab_settings.messenger = self.messenger
        