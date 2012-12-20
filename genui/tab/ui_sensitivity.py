# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sensitivity.ui'
#
# Created: Thu Dec 20 12:04:26 2012
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
        Sensitivity.resize(590, 606)
        self.horizontalLayout = QtGui.QHBoxLayout(Sensitivity)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_sens_1 = QtGui.QGroupBox(Sensitivity)
        self.groupBox_sens_1.setObjectName(_fromUtf8("groupBox_sens_1"))
        self.formLayout = QtGui.QFormLayout(self.groupBox_sens_1)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
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
        self.groupBox_13 = QtGui.QGroupBox(self.groupBox_sens_1)
        self.groupBox_13.setObjectName(_fromUtf8("groupBox_13"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.groupBox_13)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.edit_sens_output_dir = QtGui.QLineEdit(self.groupBox_13)
        self.edit_sens_output_dir.setObjectName(_fromUtf8("edit_sens_output_dir"))
        self.horizontalLayout_8.addWidget(self.edit_sens_output_dir)
        self.tool_sens_output_dir = QtGui.QToolButton(self.groupBox_13)
        self.tool_sens_output_dir.setObjectName(_fromUtf8("tool_sens_output_dir"))
        self.horizontalLayout_8.addWidget(self.tool_sens_output_dir)
        self.formLayout.setWidget(10, QtGui.QFormLayout.SpanningRole, self.groupBox_13)
        self.groupBox_sens_3 = QtGui.QGroupBox(self.groupBox_sens_1)
        self.groupBox_sens_3.setTitle(_fromUtf8(""))
        self.groupBox_sens_3.setObjectName(_fromUtf8("groupBox_sens_3"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.groupBox_sens_3)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.button_sens_start = QtGui.QPushButton(self.groupBox_sens_3)
        self.button_sens_start.setObjectName(_fromUtf8("button_sens_start"))
        self.horizontalLayout_7.addWidget(self.button_sens_start)
        self.button_sens_save = QtGui.QPushButton(self.groupBox_sens_3)
        self.button_sens_save.setObjectName(_fromUtf8("button_sens_save"))
        self.horizontalLayout_7.addWidget(self.button_sens_save)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.formLayout.setWidget(9, QtGui.QFormLayout.SpanningRole, self.groupBox_sens_3)
        self.horizontalLayout.addWidget(self.groupBox_sens_1)
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
        self.groupBox_13.setTitle(_translate("Sensitivity", "Output Dir", None))
        self.tool_sens_output_dir.setText(_translate("Sensitivity", "...", None))
        self.button_sens_start.setText(_translate("Sensitivity", "Compute", None))
        self.button_sens_save.setText(_translate("Sensitivity", "Generate tasks", None))
        self.groupBox_sens_2.setTitle(_translate("Sensitivity", "List of materials", None))

