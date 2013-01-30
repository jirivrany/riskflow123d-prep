# -*- coding: utf-8 -*-

from genui.ui_tabwidget import Ui_TabWidget
from PyQt4 import QtGui

from gui.tab.FlowCheck import FlowCheck
from gui.tab.Settings import SettingsTab
from gui.tab.Material import MaterialTab
from gui.tab.MeshSettings import MeshSettingsTab
from gui.tab.MeshTools import MeshToolsTab
from gui.tab.Sensitivity import SensitivityTab
from gui.tab.MonteCarlo import MonteCarloTab

from app.helpers.monte_logger import MonteLogger


TAB_LABELS = {
              'flow' : u'Flow ini editor',
              'settings' : u'Settings',
              'material' : u'Material Editor',
              'mesh_settings' : u'Mesh Settings',
              'mesh_tools' : u'Mesh Tools',
              'sensitivity' : u'Sensitivity',
              'monte_carlo' : u'Monte Carlo',
              }

class MainTabWidget(QtGui.QTabWidget, Ui_TabWidget):
    '''
    Factory for MainTab - creates and removes widgets
    glue them together
    '''
    
    def __init__(self, parent = None):
        super(MainTabWidget, self).__init__(parent)
        self.setupUi(self)
        
        self.tab_flow_ini = FlowCheck(self)
        self.addTab(self.tab_flow_ini, TAB_LABELS['flow'])
        
        self.tab_settings = SettingsTab(self)
        self.addTab(self.tab_settings, TAB_LABELS['settings'])
        
        self.is_ready = False
        
        
    def add_basic_problem_tabs(self):
        '''
        add tabs for basic problem
        material settings
        mesh settings and mesh tools
        ''' 
        self.remove_solver_tabs()
        
        self.__add_material_settings_tab()
        
        self.tab_mesh_settings = MeshSettingsTab(self)
        self.addTab(self.tab_mesh_settings, TAB_LABELS['mesh_settings'])
        
        self.tab_mesh_tools = MeshToolsTab(self)
        self.addTab(self.tab_mesh_tools, TAB_LABELS['mesh_tools'])
        
        self.is_ready = True
        self.setCurrentIndex(2)
                   
            
    def add_sensitivity_task_tabs(self):
        '''
        add tables for sensitivity task 
        sensitivity solver and material settings
        '''
        
        self.remove_solver_tabs()
        
        self.__add_material_settings_tab()
            
        self.tab_sensitivity = SensitivityTab(self)
        self.addTab(self.tab_sensitivity, TAB_LABELS['sensitivity'])
        
        self.is_ready = True
        self.setCurrentIndex(3)
        
    def add_monte_carlo_tabs(self):
        '''
        add tables for monte carlo task 
        monte carlo solver + material settings
        '''
        
        self.remove_solver_tabs()
        
        self.__add_material_settings_tab()    
        
        
        self.tab_montecarlo = MonteCarloTab(MonteLogger(self.window().output_dir), self)
        self.addTab(self.tab_montecarlo, TAB_LABELS['monte_carlo'])
        
        self.is_ready = True
        self.setCurrentIndex(3)
        
    def remove_solver_tabs(self):
        '''
        remove tables when switching between solver methods
        '''
        count = self.count() - 1
        while count >= 2:
            self.removeTab(count)
            count -= 1
            
    def __add_material_settings_tab(self):
        '''
        add table for material settings
        this table is common for all three tasks, nevertheless
        it has to be created after task ini file is loaded
        '''
        self.tab_material = MaterialTab(self)
        self.addTab(self.tab_material, TAB_LABELS['material'])
        
    
        
   
        
        
        
        
        
        
