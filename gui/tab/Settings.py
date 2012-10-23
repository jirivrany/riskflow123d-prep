# -*- coding: utf-8 -*-

'''
@author: Jiri Vrany

Application Settings Tab
'''

from genui.tab.ui_settings import Ui_tab_settings
from PySide.QtGui import QWidget, QFileDialog
from ast import literal_eval
from os.path import dirname


from app import Settings

class SettingsTab(QWidget, Ui_tab_settings):
    '''
    Settings Tab Widget with generated UI
    '''
    def __init__(self, parent = None):
        super(SettingsTab, self).__init__(parent)
        self.setupUi(self)
        
        #will be defined later from main window
        self.messenger = None
    
        self.buttonBox.accepted.connect(self.save)
        self.buttonBox.rejected.connect(self.load)
        
        
        
        self.setup = Settings.Settings()
        
        self.launcher_button_local.clicked.connect(self.setup_flow_exe)
        
        #fill up the form
        self.load()
        #debug
        #print self.setup
        
        
        
        
    def save(self):
        '''
        take values from form and save it to file
        '''
        self.setup.values['Launcher']['Local'] = self.launcher_check_local.isChecked()
        self.setup.values['Launcher']['Local_bin'] = self.edit_local_launcher.text()
        self.setup.values['Launcher']['Cluster'] = self.launcher_check_hydra.isChecked()
        self.setup.values['Launcher']['Cluster_bin'] = self.edit_cluster_launcher.text()
        self.setup.save_settings()
        self.messenger.speakWord.emit("Hello everybody!")
        
    def load(self):
        '''
        load saved values / discard changes
        '''
        self.setup.load_settings()
        self.launcher_check_hydra.setChecked(literal_eval(self.setup.values['Launcher']['Cluster']))
        self.edit_local_launcher.setText(self.setup.values['Launcher']['Local_bin'])
        self.launcher_check_local.setChecked(literal_eval(self.setup.values['Launcher']['Local']))
        #self.flow_exec = self.setup.values['Launcher']['Local_bin']
        self.edit_cluster_launcher.setText(self.setup.values['Launcher']['Cluster_bin'])
        
    def setup_flow_exe(self):
        '''
        setup where is flow executable located
        '''
        tmp = self._pick_up_flow_exe()
        try:
            self.flow_exec = tmp[0]
            self.edit_local_launcher.setText(tmp[0])
            self.launcher_check_local.setChecked(True)
        except TypeError:
            print("pick up of executable has failed")    
        
    def _pick_up_flow_exe(self):
        '''SetUP output using Qfiledialog'''        
        tmp =  QFileDialog.getOpenFileName(self, \
                        "Open Flow123d executable", ".", \
                        "Flow executable (*.exe)\nAll Files (*.*)")
        return tmp 