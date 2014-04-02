# -*- coding: utf-8 -*-

'''
Created on 13. 9. 2013

@author: albert
'''
from PyQt4 import QtCore, QtGui
from gui.validators import MyDoubleValidator
from gui.dialogs.SubstancesDialog import SubstancesDialog

import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
    

class Ui_Dialog(object):
    def setupUi(self, Dialog, lines=1, labels=["TextLabel"], substances=False):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(537, 150)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.label_sens_mult_1 = QtGui.QLabel(self.frame)
        self.label_sens_mult_1.setObjectName(_fromUtf8("label_sens_mult_1"))
        self.gridLayout.addWidget(self.label_sens_mult_1, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        for row_nr in range(lines):
            row_index = 1 * (1+row_nr)
            #row_number
            name_row = 'label_row_{}'.format(row_nr)
            setattr(self, name_row, QtGui.QLabel(self.frame))
            label = getattr(self, name_row)
            label.setObjectName(_fromUtf8("label_4"))
            label.setText("<html><body><center>{}</center></body></html>".format(row_index)) 
            self.gridLayout.addWidget(label, row_index, 1, 1, 1)
            
            #porosity
            name_porosity = 'edit_sens_porosity_{}'.format(row_nr)
            setattr(self, name_porosity, QtGui.QLineEdit(self.frame))
            poro = getattr(self, name_porosity) 
            poro.setMaximumSize(QtCore.QSize(80, 16777215))
            poro.setObjectName(_fromUtf8("edit_sens_porosity_1"))
            self.gridLayout.addWidget(poro, row_index, 3, 1, 1)
            #conductivity
            name_conductivity = 'edit_sens_conduct_{}'.format(row_nr)
            setattr(self, name_conductivity, QtGui.QLineEdit(self.frame))
            sens = getattr(self, name_conductivity)
            sens.setMaximumSize(QtCore.QSize(80, 16777215))
            sens.setObjectName(_fromUtf8("edit_sens_conduct_1"))
            self.gridLayout.addWidget(sens, row_index, 2, 1, 1)
            #storativity
            name_storativity = 'edit_sens_storativity_{}'.format(row_nr)
            setattr(self, name_storativity, QtGui.QLineEdit(self.frame))
            storativity = getattr(self, name_storativity)
            storativity.setMaximumSize(QtCore.QSize(80, 16777215))
            storativity.setObjectName(_fromUtf8("edit_sens_storativity_1"))
            self.gridLayout.addWidget(storativity, row_index, 4, 1, 1)
            #sorption substances
            if substances:
                name_sorption = 'button_sens_sorption_{}'.format(row_nr)
                setattr(self, name_sorption, QtGui.QPushButton(self.frame))
                sorption = getattr(self, name_sorption)
                sorption.setObjectName(_fromUtf8("button_sens_sorption_1"))
                sorption.setText(_translate("Dialog", "sorption", None))
                self.gridLayout.addWidget(sorption, row_index, 5, 1, 1)
                
        
        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Conductivity", None))
        self.label_2.setText(_translate("Dialog", "Storativity", None))
        self.label_3.setText(_translate("Dialog", "Porosity", None))
        self.label_sens_mult_1.setText(_translate("Dialog", "Multiplier for", None))
           

class SensitivityDialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, lines=1, values={'1': '0.0'}, parent=None, labels=None, substances=False):
        '''
        lines - number of lines in dialog
        values - dict with dialog values and labels
        labels - but labels can be set separately
        '''
        QtGui.QDialog.__init__(self, parent)
        if not labels:
            labels = sorted(values.keys())
        self.setupUi(self, lines, labels, substances)
        self.lines = lines
        if substances:
            self.connect_substance_buttons(lines)
        
        
    def connect_substance_buttons(self, lines):
        for line_nr in range(lines):
            name = 'button_sens_sorption_{}'.format(line_nr)
            getattr(self, name).clicked.connect(self.sorption_substance_subdialog)    
        
    def set_initial_values(self, values):
        
        for line_nr, line_value in values.iteritems():
            namme = 'line_edit_{}'.format(line_nr)
            getattr(self, namme).setText(line_value)
            
            
    def sorption_substance_subdialog(self):
        '''
        dialog for sorption substances
        '''
            
        dlg = SubstancesDialog(lines=2)
        if dlg.exec_():
            pattern = 'button_sens_sorption_'
            sender = self.sender().objectName()
            sender = str(sender[len(pattern):])
            
            print dlg.get_values()
            
                
        
    def get_values(self):
        values = {}
        for line_nr in range(self.lines):
            namme = 'line_edit_{}'.format(line_nr)
            value = getattr(self, namme).text()
            if not value:
                value = 0.0
            values[str(line_nr)] = str(value)
        
        return values
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = SensitivityDialog(lines=15, substances=True)
    form.exec_()        

