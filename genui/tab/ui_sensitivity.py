# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sensitivity.ui'
#
# Created: Thu Apr  3 07:55:45 2014
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

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

class Ui_Sensitivity(object):
    def setupUi(self, Sensitivity):
        Sensitivity.setObjectName(_fromUtf8("Sensitivity"))
        Sensitivity.resize(1007, 667)
        self.horizontalLayout = QtGui.QHBoxLayout(Sensitivity)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.frame_2 = QtGui.QFrame(Sensitivity)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_sens_1 = QtGui.QGroupBox(self.frame_2)
        self.groupBox_sens_1.setObjectName(_fromUtf8("groupBox_sens_1"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_sens_1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.edit_sens_num_lines = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_num_lines.setMaximumSize(QtCore.QSize(80, 16777215))
        self.edit_sens_num_lines.setObjectName(_fromUtf8("edit_sens_num_lines"))
        self.gridLayout.addWidget(self.edit_sens_num_lines, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_sens_1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.button_sens_lines_dialog = QtGui.QPushButton(self.groupBox_sens_1)
        self.button_sens_lines_dialog.setObjectName(_fromUtf8("button_sens_lines_dialog"))
        self.gridLayout.addWidget(self.button_sens_lines_dialog, 1, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_sens_1)
        self.groupBox_sens_3 = QtGui.QGroupBox(self.frame_2)
        self.groupBox_sens_3.setTitle(_fromUtf8(""))
        self.groupBox_sens_3.setObjectName(_fromUtf8("groupBox_sens_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_sens_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.button_sens_cross = QtGui.QPushButton(self.groupBox_sens_3)
        self.button_sens_cross.setObjectName(_fromUtf8("button_sens_cross"))
        self.verticalLayout_3.addWidget(self.button_sens_cross)
        self.button_sens_group = QtGui.QPushButton(self.groupBox_sens_3)
        self.button_sens_group.setObjectName(_fromUtf8("button_sens_group"))
        self.verticalLayout_3.addWidget(self.button_sens_group)
        self.verticalLayout_2.addWidget(self.groupBox_sens_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.frame_2)
        self.groupBox_sens_2 = QtGui.QGroupBox(Sensitivity)
        self.groupBox_sens_2.setObjectName(_fromUtf8("groupBox_sens_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_sens_2)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.list_sens_mtr = QtGui.QListWidget(self.groupBox_sens_2)
        self.list_sens_mtr.setObjectName(_fromUtf8("list_sens_mtr"))
        self.verticalLayout_6.addWidget(self.list_sens_mtr)
        self.horizontalLayout.addWidget(self.groupBox_sens_2)

        self.retranslateUi(Sensitivity)
        QtCore.QMetaObject.connectSlotsByName(Sensitivity)

    def retranslateUi(self, Sensitivity):
        Sensitivity.setWindowTitle(_translate("Sensitivity", "Form", None))
        self.groupBox_sens_1.setTitle(_translate("Sensitivity", "Choose multiplier for material property", None))
        self.label_4.setText(_translate("Sensitivity", "number of multipliers:", None))
        self.button_sens_lines_dialog.setText(_translate("Sensitivity", "choose", None))
        self.button_sens_cross.setText(_translate("Sensitivity", "Multiplier x Material ", None))
        self.button_sens_group.setText(_translate("Sensitivity", "Multiplier x Group of materials", None))
        self.groupBox_sens_2.setTitle(_translate("Sensitivity", "List of materials", None))

