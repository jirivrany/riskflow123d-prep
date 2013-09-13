# -*- coding: utf-8 -*-

'''
Created on 13. 9. 2013

@author: albert
'''
from PyQt4 import QtCore, QtGui

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
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(389, 293)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 10, 381, 261))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayout = QtGui.QFormLayout(self.frame)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        for line_in in range(lines):
            namme = 'line_edit_{}'.format(line_in)
            namel = 'label_{}'.format(line_in)
            namme = 'line_edit_{}'.format(line_in)
            namel = 'label_{}'.format(line_in)
            setattr(self, namme , QtGui.QLineEdit(self.frame))
            new_edit = getattr(self, namme)
            new_edit.setObjectName(_fromUtf8(namme)) 
            self.formLayout.setWidget(1 * line_in, QtGui.QFormLayout.FieldRole, new_edit)
            setattr(self, namel , QtGui.QLabel(self.frame))
            new_label = getattr(self, namel)
            new_label.setObjectName(_fromUtf8(namel))
            self.formLayout.setWidget(1 * line_in, QtGui.QFormLayout.LabelRole, new_label)
        
        self.buttonBox = QtGui.QDialogButtonBox(self.frame)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(Dialog, labels)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog, labels):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        for line_in, label in enumerate(labels):
            namel = 'label_{}'.format(line_in)
            getattr(self, namel).setText(_translate("Dialog", label, None))




class SubstancesDialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, lines=1, labels=['Label'], parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self, lines, labels)
        self.lines = lines
        
    def get_values(self):
        values = {}
        for line_nr in range(self.lines):
            namme = 'line_edit_{}'.format(line_nr)
            value = getattr(self, namme).text()
            values[line_nr] = str(value)
        
        return values    

