# -*- coding: utf-8 -*-
'''
@author: Jiri Vrany

MainWindow of the app. 
Class
'''

from PyQt4.QtGui import QMainWindow, QFileDialog


from gui.MainTabWidget import MainTabWidget
from gui.MainMenu import MainMenu
from gui.MainStatusBar import MainStatusBar
import gui.toolbar

from app.FlowIni import FlowIni

from app.helpers import constants as const
 
import app.helpers.output_dir
import app.helpers.solver_utils

import app.parser.material as material




class MainWindow(QMainWindow):
    '''
    Main Application Window
    Factory for main widgets - action bar and tool bar, central tab
    Glue all Widgets together
    '''
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(800, 600)
        
        #central widget is tab
        self.centralWidget = MainTabWidget(self)
        self.setCentralWidget(self.centralWidget)
        
        #main menu of window
        self.menuBar = MainMenu(self)
        self.setMenuBar(self.menuBar)
        self.set_menubar_actions()
        
        #status bar
        self.statusBar = MainStatusBar(self)
        self.setStatusBar(self.statusBar)
        
        self.toolBar = gui.toolbar.MainToolBar(self)
        self.addToolBar(self.toolBar)
        self.action_exit = gui.toolbar.ExitAction()
        self.action_solve = gui.toolbar.SolveAction()
        self.action_quick_start = gui.toolbar.QuickStartAction()
        
        self.set_toolbar_actions()
        
        #app object
        self.flow_ini = None
        self.material_dict = None
        
        #let's roll
        #self.quick_start()
    
    def hello(self):
        print 'hello'
        
    def set_toolbar_actions(self):
        '''
        set the actions for toolbar
        '''
        
        self.toolBar.addAction(self.action_quick_start)
        self.toolBar.addAction(self.action_solve)
        self.toolBar.addAction(self.action_exit)
        self.action_exit.triggered.connect(self.on_app_exit)
        self.action_solve.triggered.connect(self.hello)
        self.action_quick_start.triggered.connect(self.quick_start)       
            
    def set_menubar_actions(self):
        '''
        set actions for menubar
        '''
        self.menuBar.actionOpen.triggered.connect(self.on_ini_file_open)
        self.menuBar.actionExit.triggered.connect(self.on_app_exit)
        self.menuBar.actionSave.triggered.connect(self.on_ini_file_save)
        
        self.menuBar.actionMonte_Carlo.triggered.connect( \
                             self.centralWidget.add_monte_carlo_tabs )
        self.menuBar.actionBasic_Problem.triggered.connect(self.on_action_basic_problem)
        self.menuBar.actionSensitivy_task.triggered.connect( \
                             self.centralWidget.add_sensitivity_task_tabs )
    
    def quick_start(self):
        '''
        quick start last edited ini file
        '''
        file_name = '/development/python/RF_test_data/test_dir_create/flow_t.ini'
        #last_ini = self.setup['Work']['Last']
        self.start_main_routine(file_name)
        
    def on_ini_file_open(self):
        '''
        Action onOpen handler 
        opens file using QFileDialog
        '''
        filetuple = QFileDialog.getOpenFileName(self, \
                        "Open File", ".", \
                        "Flow ini (*.ini)\nAll Files (*.*)")
        fname = filetuple[0]
        self.start_main_routine(fname)
        
    def start_main_routine(self, fname):
        '''
        Call handler in tab_flow_ini Widget
        Calls Factory methods for Material and Mesh objects
        Display result message 
        '''     
        try:
            self.flow_ini = FlowIni(fname)
        except TypeError:
            self.statusBar.showMessage("Nothing to do", 500) 
        finally:        
            if self.centralWidget.tab_flow_ini.handle_file(self.flow_ini):
                self.load_material()
                self.load_mesh()
            else:
                self.statusBar.showMessage('ERROR in ini file', 8000)
                
    def on_ini_file_save(self):
        '''
        Action onSave handler
        save changes from editor
        '''
        fname = self.flow_ini.file_name
        if self.centralWidget.tab_flow_ini.dialog_ini_file_save(fname):
            self.start_main_routine(fname)
            
                
    def load_material(self):
        '''
        Executed after sucessfull check of flow.ini file
        Factory for MaterialDict - prepares object for application
        '''
        try:
            self.material_dict = material.MaterialDict(self.flow_ini.get_material_file_name())
        except material.EmptyListException:
            self.statusBar.showMessage('Error loading material from file', 8000)
        finally:
            self.statusBar.showMessage('Material file loaded', 8000)
    
    def load_mesh(self):
        '''
        Executed after sucessfull check of flow.ini file
        Factory for Mesh - prepares object for application
        '''            
        pass
    
                
    def on_app_exit(self):
        '''
        When user exit the app by button
        Save last used ini file for quick start next time
        '''
        setup = self.centralWidget.tab_settings.setup
        try:
            setup.values['Work']['Last'] = self.flow_ini.file_name
        except AttributeError:
            pass    
        setup.save_settings()
        self.close()
        
    def on_action_basic_problem(self):
        '''
        slot for action basic problem signal
        prepares all necesities for basic solver problem
        '''
        self.centralWidget.add_basic_problem_tabs
        
        
        output_dir = app.helpers.output_dir.set_output_dir(\
                               self.flow_ini.dir_name, 'basic', const.SEPARATOR)
        result = app.helpers.output_dir.create_if_not_exists(output_dir)
        
        self.statusBar.showMessage(result, 8000)
        
        app.helpers.solver_utils.copy_master_files(self.flow_ini, output_dir, const.SEPARATOR)
           