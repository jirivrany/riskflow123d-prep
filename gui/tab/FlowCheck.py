# -*- coding: utf-8 -*-

'''
@author: Jiri Vrany

Editor and test for flow.ini file. Tab Widget.
'''

from genui.tab.ui_flow_check import Ui_tab_8
from PySide import QtGui
from os.path import isfile

from app.parser import flow
from app.Settings import SEPARATOR

class FlowCheck(QtGui.QWidget, Ui_tab_8):
    '''
    Tab Widget with generated UI
    '''
    def __init__(self, parent = None):
        super(FlowCheck, self).__init__(parent)
        self.setupUi(self)
        
        #will be defined later from main window
        self.messenger = None
        
    
    def handle_file(self, ini_file):
        '''
        @param ini_file object class FlowIni()
        '''
        message = ""
        if not self._set_labels_from_dict(ini_file.dict_files, ini_file.dir_name):
            message += "Missing some required files, please check your flow.ini"
        if not self._set_editor_text(ini_file.text):
            message += "Failed to populate editor windows"
            
        return message    
        
    def _set_labels_from_dict(self, file_dict, ini_dir):
        '''
        set labels in editor
        @param file_dict = dict of files from FlowIni()
        @param ini_rid  = flow ini dir, in FlowIni()
        ''' 
        
        everything_ok = True
        
        print file_dict

        for key, name in flow.EXTENSIONS_DICT['Input'].iteritems():
            
            temp_name = ini_dir + SEPARATOR + file_dict[key]
            print temp_name
            test = isfile(temp_name)
            print key, name, test
            ltext = flow.LABELS_DICT[key]
            label = 'label_'+ltext
            line = 'lineEdit_'+ltext
            try:
                current_label = getattr(self, label)
                current_line = getattr(self, line)
                if test:
                    current_label.setText('OK')
                    current_line.setText(temp_name)
                else:
                    current_label.setText('FAIL')
                    current_line.setText(temp_name)
                    everything_ok = False 
            
            except AttributeError:
                return False
        
        return everything_ok     
            


    def _set_editor_text(self, text):
        '''
        @param text / text to be set in flow editor window
        '''
        
        self.edit_flow_ini.setPlainText(text)
        return True        