# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sensitivity.ui'
#
# Created: Tue Jan 15 10:33:04 2013
#      by: PyQt4 UI code generator 4.9.6
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
        Sensitivity.resize(625, 667)
        self.horizontalLayout = QtGui.QHBoxLayout(Sensitivity)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.frame_2 = QtGui.QFrame(Sensitivity)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_sens_1 = QtGui.QGroupBox(self.frame_2)
        self.groupBox_sens_1.setObjectName(_fromUtf8("groupBox_sens_1"))
        self.formLayout = QtGui.QFormLayout(self.groupBox_sens_1)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_sens_mult_1 = QtGui.QLabel(self.groupBox_sens_1)
        self.label_sens_mult_1.setObjectName(_fromUtf8("label_sens_mult_1"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_sens_mult_1)
        self.edit_sens_mult_1 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_mult_1.setObjectName(_fromUtf8("edit_sens_mult_1"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.edit_sens_mult_1)
        self.label_sens_mult_2 = QtGui.QLabel(self.groupBox_sens_1)
        self.label_sens_mult_2.setObjectName(_fromUtf8("label_sens_mult_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_sens_mult_2)
        self.edit_sens_mult_2 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_mult_2.setObjectName(_fromUtf8("edit_sens_mult_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.edit_sens_mult_2)
        self.label_sens_mult_3 = QtGui.QLabel(self.groupBox_sens_1)
        self.label_sens_mult_3.setObjectName(_fromUtf8("label_sens_mult_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_sens_mult_3)
        self.edit_sens_mult_3 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_mult_3.setObjectName(_fromUtf8("edit_sens_mult_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.edit_sens_mult_3)
        self.label_sens_mult_4 = QtGui.QLabel(self.groupBox_sens_1)
        self.label_sens_mult_4.setObjectName(_fromUtf8("label_sens_mult_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_sens_mult_4)
        self.edit_sens_mult_4 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_mult_4.setObjectName(_fromUtf8("edit_sens_mult_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.edit_sens_mult_4)
        self.label_sens_mult_5 = QtGui.QLabel(self.groupBox_sens_1)
        self.label_sens_mult_5.setObjectName(_fromUtf8("label_sens_mult_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_sens_mult_5)
        self.edit_sens_mult_5 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_mult_5.setObjectName(_fromUtf8("edit_sens_mult_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.edit_sens_mult_5)
        self.label_sens_mult_6 = QtGui.QLabel(self.groupBox_sens_1)
        self.label_sens_mult_6.setObjectName(_fromUtf8("label_sens_mult_6"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_sens_mult_6)
        self.edit_sens_mult_6 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_mult_6.setObjectName(_fromUtf8("edit_sens_mult_6"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.edit_sens_mult_6)
        self.label_sens_mult_7 = QtGui.QLabel(self.groupBox_sens_1)
        self.label_sens_mult_7.setObjectName(_fromUtf8("label_sens_mult_7"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_sens_mult_7)
        self.edit_sens_mult_7 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_mult_7.setObjectName(_fromUtf8("edit_sens_mult_7"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.edit_sens_mult_7)
        self.label_sens_mult_8 = QtGui.QLabel(self.groupBox_sens_1)
        self.label_sens_mult_8.setObjectName(_fromUtf8("label_sens_mult_8"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_sens_mult_8)
        self.edit_sens_mult_8 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_mult_8.setObjectName(_fromUtf8("edit_sens_mult_8"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.edit_sens_mult_8)
        self.verticalLayout_2.addWidget(self.groupBox_sens_1)
        self.groupBox = QtGui.QGroupBox(self.frame_2)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.check_cond = QtGui.QCheckBox(self.groupBox)
        self.check_cond.setObjectName(_fromUtf8("check_cond"))
        self.verticalLayout.addWidget(self.check_cond)
        self.check_storat = QtGui.QCheckBox(self.groupBox)
        self.check_storat.setObjectName(_fromUtf8("check_storat"))
        self.verticalLayout.addWidget(self.check_storat)
        self.check_porosity = QtGui.QCheckBox(self.groupBox)
        self.check_porosity.setObjectName(_fromUtf8("check_porosity"))
        self.verticalLayout.addWidget(self.check_porosity)
        self.verticalLayout_2.addWidget(self.groupBox)
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
        self.groupBox_sens_1.setTitle(_translate("Sensitivity", "Multiplicator form", None))
        self.label_sens_mult_1.setText(_translate("Sensitivity", "Multiplicator #1", None))
        self.label_sens_mult_2.setText(_translate("Sensitivity", "Multiplicator #2", None))
        self.label_sens_mult_3.setText(_translate("Sensitivity", "Multiplicator #3", None))
        self.label_sens_mult_4.setText(_translate("Sensitivity", "Multiplicator #4", None))
        self.label_sens_mult_5.setText(_translate("Sensitivity", "Multiplicator #5", None))
        self.label_sens_mult_6.setText(_translate("Sensitivity", "Multiplicator #6", None))
        self.label_sens_mult_7.setText(_translate("Sensitivity", "Multiplicator #7", None))
        self.label_sens_mult_8.setText(_translate("Sensitivity", "Multiplicator #8", None))
        self.groupBox.setTitle(_translate("Sensitivity", "Compute with", None))
        self.check_cond.setText(_translate("Sensitivity", "Hydraulic conductivity", None))
        self.check_storat.setText(_translate("Sensitivity", "Storativity", None))
        self.check_porosity.setText(_translate("Sensitivity", "Dual porosity", None))
        self.button_sens_cross.setText(_translate("Sensitivity", "multiplicator x Material ", None))
        self.button_sens_group.setText(_translate("Sensitivity", "multiplicator x Group of materials", None))
        self.groupBox_sens_2.setTitle(_translate("Sensitivity", "List of materials", None))

