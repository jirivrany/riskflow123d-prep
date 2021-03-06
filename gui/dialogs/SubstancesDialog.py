# -*- coding: utf-8 -*-

'''

Dialog for Sensitivity Task values 

@author: albert
'''
from PyQt4 import QtCore, QtGui
from gui.validators import MyDoubleValidator

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
    def setupUi(self, Dialog, lines=1, labels=["TextLabel"]):
        width = 200
        height = lines * 40 + 50
        
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(width, height)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 10, width, height))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayout = QtGui.QFormLayout(self.frame)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        
        self.label_col1 = QtGui.QLabel(self.frame)
        self.label_col1.setText('substance')
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_col1)
        
        self.label_col2 = QtGui.QLabel(self.frame)
        self.label_col2.setText('sorption value')
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_col2)

        validator_positive_double = MyDoubleValidator(True, self)

        for line_in in range(lines):
            row_index = 1 * (1+line_in)
            namme = 'line_edit_{}'.format(line_in)
            namel = 'label_{}'.format(line_in)
            namme = 'line_edit_{}'.format(line_in)
            namel = 'label_{}'.format(line_in)
            setattr(self, namme , QtGui.QLineEdit(self.frame))
            new_edit = getattr(self, namme)
            new_edit.setObjectName(_fromUtf8(namme))
            new_edit.setValidator(validator_positive_double) 
            self.formLayout.setWidget(row_index, QtGui.QFormLayout.FieldRole, new_edit)
            setattr(self, namel , QtGui.QLabel(self.frame))
            new_label = getattr(self, namel)
            new_label.setObjectName(_fromUtf8(namel))
            new_label.setAlignment(QtCore.Qt.AlignCenter)
            self.formLayout.setWidget(row_index, QtGui.QFormLayout.LabelRole, new_label)
        
        self.buttonBox = QtGui.QDialogButtonBox(self.frame)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.buttonBox)
        
        

        self.retranslateUi(Dialog, labels)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog, labels):
        Dialog.setWindowTitle(_translate("Dialog", "Sorption Substances", None))
        for line_in, label in enumerate(labels):
            namel = 'label_{}'.format(line_in)
            getattr(self, namel).setText(_translate("Dialog", label, None))




class SubstancesDialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, lines=1, values={'1': '0.0'}, parent=None, labels=None):
        '''
        lines - number of lines in dialog
        values - dict with dialog values and labels
        labels - but labels can be set separately
        '''
        QtGui.QDialog.__init__(self, parent)
        if not labels:
            labels = sorted(values.keys())
        self.setupUi(self, lines, labels)
        self.lines = lines
        self.set_initial_values(values)
        
    def set_initial_values(self, values):
        
        for line_nr, line_value in values.iteritems():
            namme = 'line_edit_{}'.format(line_nr)
            getattr(self, namme).setText(line_value)
            
        
    def get_values(self):
        values = {}
        for line_nr in range(self.lines):
            namme = 'line_edit_{}'.format(line_nr)
            value = getattr(self, namme).text()
            if not value:
                value = 0.0
            values[str(line_nr)] = str(value)
        
        return values    

