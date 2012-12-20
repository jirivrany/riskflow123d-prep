# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'meshtools.ui'
#
# Created: Thu Dec 20 12:04:16 2012
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

class Ui_MeshTools(object):
    def setupUi(self, MeshTools):
        MeshTools.setObjectName(_fromUtf8("MeshTools"))
        MeshTools.resize(574, 537)
        self.gridLayout = QtGui.QGridLayout(MeshTools)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_10 = QtGui.QGroupBox(MeshTools)
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBox_10)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.label_9 = QtGui.QLabel(self.groupBox_10)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_9.addWidget(self.label_9, 0, 0, 1, 1)
        self.edit_multiply_conduct = QtGui.QLineEdit(self.groupBox_10)
        self.edit_multiply_conduct.setObjectName(_fromUtf8("edit_multiply_conduct"))
        self.gridLayout_9.addWidget(self.edit_multiply_conduct, 0, 1, 1, 1)
        self.button_multiply_conduct = QtGui.QPushButton(self.groupBox_10)
        self.button_multiply_conduct.setObjectName(_fromUtf8("button_multiply_conduct"))
        self.gridLayout_9.addWidget(self.button_multiply_conduct, 0, 2, 1, 1)
        self.edit_nvalue_conduct = QtGui.QLineEdit(self.groupBox_10)
        self.edit_nvalue_conduct.setObjectName(_fromUtf8("edit_nvalue_conduct"))
        self.gridLayout_9.addWidget(self.edit_nvalue_conduct, 1, 1, 1, 1)
        self.button_nvalue_conduct = QtGui.QPushButton(self.groupBox_10)
        self.button_nvalue_conduct.setObjectName(_fromUtf8("button_nvalue_conduct"))
        self.gridLayout_9.addWidget(self.button_nvalue_conduct, 1, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_10)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_9.addWidget(self.label_10, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_10, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(142, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.groupBox_11 = QtGui.QGroupBox(MeshTools)
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.gridLayout_11 = QtGui.QGridLayout(self.groupBox_11)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.button_gen_mtr_all = QtGui.QPushButton(self.groupBox_11)
        self.button_gen_mtr_all.setObjectName(_fromUtf8("button_gen_mtr_all"))
        self.gridLayout_11.addWidget(self.button_gen_mtr_all, 0, 0, 1, 1)
        self.button_gen_mtr_selected = QtGui.QPushButton(self.groupBox_11)
        self.button_gen_mtr_selected.setObjectName(_fromUtf8("button_gen_mtr_selected"))
        self.gridLayout_11.addWidget(self.button_gen_mtr_selected, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox_11, 1, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 363, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)

        self.retranslateUi(MeshTools)
        QtCore.QMetaObject.connectSlotsByName(MeshTools)

    def retranslateUi(self, MeshTools):
        MeshTools.setWindowTitle(_translate("MeshTools", "Form", None))
        self.groupBox_10.setTitle(_translate("MeshTools", "Operation with group of mesh elements", None))
        self.label_9.setText(_translate("MeshTools", "Multiply Hydraulic Conductivity by:", None))
        self.button_multiply_conduct.setText(_translate("MeshTools", "OK", None))
        self.button_nvalue_conduct.setText(_translate("MeshTools", "OK", None))
        self.label_10.setText(_translate("MeshTools", "Set Hydraulict Conductivity to:", None))
        self.groupBox_11.setTitle(_translate("MeshTools", "Generate unique material for each element", None))
        self.button_gen_mtr_all.setText(_translate("MeshTools", "in Mesh File (all)", None))
        self.button_gen_mtr_selected.setText(_translate("MeshTools", "in Mesh List (selected)", None))

