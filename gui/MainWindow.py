# -*- coding: utf-8 -*-
'''
@author: Jiri Vrany

MainWindow of the app. 
Class
'''

from genui.main_window import Ui_MainWindow
from PySide.QtGui import QMainWindow, QFileDialog


from gui.MainTabWidget import MainTabWidget
from gui.MainMenu import MainMenu
from gui.MainStatusBar import MainStatusBar

from app.FlowIni import FlowIni



class MainWindow(QMainWindow, Ui_MainWindow):
    '''
    Main Application Window
    Factory for main widgets - action bar and tool bar, central tab
    Glue all Widgets together
    '''
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
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
        self.flow_ini = None
    
    def set_menubar_actions(self):
        '''
        set actions for menubar
        '''
        self.menuBar.actionOpen.triggered.connect(self.on_ini_file_open)
        self.menuBar.actionExit.triggered.connect(self.on_app_exit)
        
        self.menuBar.actionMonte_Carlo.triggered.connect( \
                             self.centralWidget.add_monte_carlo_tabs )
        self.menuBar.actionBasic_Problem.triggered.connect( \
                             self.centralWidget.add_basic_problem_tabs )
        self.menuBar.actionSensitivy_task.triggered.connect( \
                             self.centralWidget.add_sensitivity_task_tabs )
        
    def on_ini_file_open(self):
        '''
        Open a flow ini file using FileDialog
        Call handler in tab_flow_ini Widget
        Display result message 
        '''
        filetuple = QFileDialog.getOpenFileName(self, \
                        "Open File", ".", \
                        "Flow ini (*.ini)\nAll Files (*.*)")
        fname = filetuple[0]
        try:
            self.flow_ini = FlowIni(fname)
        except TypeError:
            self.statusBar.set_message("Nothing to do", 500) 
        finally:        
            self.centralWidget.tab_flow_ini.handle_file(self.flow_ini)
                
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