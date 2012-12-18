# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'meshtools.ui'
#
# Created: Tue Dec 04 17:31:14 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MeshTools(object):
    def setupUi(self, MeshTools):
        MeshTools.setObjectName("MeshTools")
        MeshTools.resize(574, 537)
        self.gridLayout = QtGui.QGridLayout(MeshTools)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_10 = QtGui.QGroupBox(MeshTools)
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBox_10)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_9 = QtGui.QLabel(self.groupBox_10)
        self.label_9.setObjectName("label_9")
        self.gridLayout_9.addWidget(self.label_9, 0, 0, 1, 1)
        self.edit_multiply_conduct = QtGui.QLineEdit(self.groupBox_10)
        self.edit_multiply_conduct.setObjectName("edit_multiply_conduct")
        self.gridLayout_9.addWidget(self.edit_multiply_conduct, 0, 1, 1, 1)
        self.button_multiply_conduct = QtGui.QPushButton(self.groupBox_10)
        self.button_multiply_conduct.setObjectName("button_multiply_conduct")
        self.gridLayout_9.addWidget(self.button_multiply_conduct, 0, 2, 1, 1)
        self.edit_nvalue_conduct = QtGui.QLineEdit(self.groupBox_10)
        self.edit_nvalue_conduct.setObjectName("edit_nvalue_conduct")
        self.gridLayout_9.addWidget(self.edit_nvalue_conduct, 1, 1, 1, 1)
        self.button_nvalue_conduct = QtGui.QPushButton(self.groupBox_10)
        self.button_nvalue_conduct.setObjectName("button_nvalue_conduct")
        self.gridLayout_9.addWidget(self.button_nvalue_conduct, 1, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_10)
        self.label_10.setObjectName("label_10")
        self.gridLayout_9.addWidget(self.label_10, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_10, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(142, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.groupBox_11 = QtGui.QGroupBox(MeshTools)
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_11 = QtGui.QGridLayout(self.groupBox_11)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.button_gen_mtr_all = QtGui.QPushButton(self.groupBox_11)
        self.button_gen_mtr_all.setObjectName("button_gen_mtr_all")
        self.gridLayout_11.addWidget(self.button_gen_mtr_all, 0, 0, 1, 1)
        self.button_gen_mtr_selected = QtGui.QPushButton(self.groupBox_11)
        self.button_gen_mtr_selected.setObjectName("button_gen_mtr_selected")
        self.gridLayout_11.addWidget(self.button_gen_mtr_selected, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox_11, 1, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 363, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)

        self.retranslateUi(MeshTools)
        QtCore.QMetaObject.connectSlotsByName(MeshTools)

    def retranslateUi(self, MeshTools):
        MeshTools.setWindowTitle(QtGui.QApplication.translate("MeshTools", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_10.setTitle(QtGui.QApplication.translate("MeshTools", "Operation with group of mesh elements", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MeshTools", "Multiply Hydraulic Conductivity by:", None, QtGui.QApplication.UnicodeUTF8))
        self.button_multiply_conduct.setText(QtGui.QApplication.translate("MeshTools", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.button_nvalue_conduct.setText(QtGui.QApplication.translate("MeshTools", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MeshTools", "Set Hydraulict Conductivity to:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_11.setTitle(QtGui.QApplication.translate("MeshTools", "Generate unique material for each element", None, QtGui.QApplication.UnicodeUTF8))
        self.button_gen_mtr_all.setText(QtGui.QApplication.translate("MeshTools", "in Mesh File (all)", None, QtGui.QApplication.UnicodeUTF8))
        self.button_gen_mtr_selected.setText(QtGui.QApplication.translate("MeshTools", "in Mesh List (selected)", None, QtGui.QApplication.UnicodeUTF8))

