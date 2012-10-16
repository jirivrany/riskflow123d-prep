# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Tue Oct 16 13:25:08 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!
from genui.tab.ui_flow_check import Ui_Tab8
from PySide import QtGui

from app.parser import flow

class FlowCheck(QtGui.QWidget, Ui_Tab8):
    
    def __init__(self, parent = None):
        super(FlowCheck, self).__init__(parent)
        self.setupUi(self)
        self.test_file()


    def test_file(self):
        fname = 'flow_test.ini'
        ini_file = flow.openFile(fname)
        self.flow_ini = flow.parser(ini_file)
        self.file_dict = flow.getDictFromFile(fname)
        
        #read file once again
        ini_file.seek(0)
        text = ini_file.read()
        self.edit_flow_ini.setPlainText(text)
        ini_file.close()
        