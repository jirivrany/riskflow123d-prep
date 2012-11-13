# -*- coding: utf-8 -*-
'''
@author: Jiri Vrany

MainWindow of the app. 
Class
'''

from genui.main_window import Ui_MainWindow
from PySide.QtGui import QMainWindow, QFileDialog


from app.FlowIni import FlowIni

from gui.MainTabWidget import MainTabWidget
from gui.MainMenu import MainMenu
from gui.MainStatusBar import MainStatusBar




class MainWindow(QMainWindow, Ui_MainWindow):
    '''
    Main Application Window
    Glue all Widgets together
    '''
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
       
        
        #central widget is tab
        self.centralWidget = MainTabWidget()
        self.setCentralWidget(self.centralWidget)
        
        
        #main menu of window
        self.menuBar = MainMenu()
        self.setMenuBar(self.menuBar)
        self.menuBar.actionOpen.triggered.connect(self.on_ini_file_open)
        self.menuBar.actionExit.triggered.connect(self.on_app_exit)
        
        #status bar
        self.statusBar = MainStatusBar()
        self.setStatusBar(self.statusBar)
        
        self.centralWidget.messenger.send_msg.connect(self.statusBar.set_message)
        
        self.flow_ini = None
        
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
            message = self.centralWidget.tab_flow_ini.handle_file(self.flow_ini)
            if message:
                self.statusBar.set_message(message)
                
    def on_app_exit(self):
        '''
        When user exit the app by button
        Save last used ini file for quick start next time
        '''
        setup = self.centralWidget.tab_settings.setup
        setup.values['Work']['Last'] = self.flow_ini.file_name
        setup.save_settings()
        self.close()  