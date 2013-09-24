# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'meshtools.ui'
#
# Created: Tue Sep 24 12:35:37 2013
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
        self.formLayout = QtGui.QFormLayout(MeshTools)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.groupBox_10 = QtGui.QGroupBox(MeshTools)
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBox_10)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.groupBox = QtGui.QGroupBox(self.groupBox_10)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.edit_multiply_conduct = QtGui.QLineEdit(self.groupBox)
        self.edit_multiply_conduct.setObjectName(_fromUtf8("edit_multiply_conduct"))
        self.gridLayout_2.addWidget(self.edit_multiply_conduct, 0, 1, 1, 1)
        self.button_multiply_conduct = QtGui.QPushButton(self.groupBox)
        self.button_multiply_conduct.setObjectName(_fromUtf8("button_multiply_conduct"))
        self.gridLayout_2.addWidget(self.button_multiply_conduct, 0, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.edit_nvalue_conduct = QtGui.QLineEdit(self.groupBox)
        self.edit_nvalue_conduct.setObjectName(_fromUtf8("edit_nvalue_conduct"))
        self.gridLayout_2.addWidget(self.edit_nvalue_conduct, 1, 1, 1, 1)
        self.button_nvalue_conduct = QtGui.QPushButton(self.groupBox)
        self.button_nvalue_conduct.setObjectName(_fromUtf8("button_nvalue_conduct"))
        self.gridLayout_2.addWidget(self.button_nvalue_conduct, 1, 2, 1, 1)
        self.edit_nvalue_conduct_y = QtGui.QLineEdit(self.groupBox)
        self.edit_nvalue_conduct_y.setObjectName(_fromUtf8("edit_nvalue_conduct_y"))
        self.gridLayout_2.addWidget(self.edit_nvalue_conduct_y, 2, 1, 1, 1)
        self.edit_nvalue_conduct_z = QtGui.QLineEdit(self.groupBox)
        self.edit_nvalue_conduct_z.setObjectName(_fromUtf8("edit_nvalue_conduct_z"))
        self.gridLayout_2.addWidget(self.edit_nvalue_conduct_z, 3, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox_10)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)
        self.button_nvalue_storativity = QtGui.QPushButton(self.groupBox_2)
        self.button_nvalue_storativity.setObjectName(_fromUtf8("button_nvalue_storativity"))
        self.gridLayout_3.addWidget(self.button_nvalue_storativity, 0, 2, 1, 1)
        self.edit_nvalue_storativity = QtGui.QLineEdit(self.groupBox_2)
        self.edit_nvalue_storativity.setObjectName(_fromUtf8("edit_nvalue_storativity"))
        self.gridLayout_3.addWidget(self.edit_nvalue_storativity, 0, 1, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_10)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_14 = QtGui.QLabel(self.groupBox_3)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_4.addWidget(self.label_14, 0, 0, 1, 1)
        self.edit_nvalue_porosity = QtGui.QLineEdit(self.groupBox_3)
        self.edit_nvalue_porosity.setObjectName(_fromUtf8("edit_nvalue_porosity"))
        self.gridLayout_4.addWidget(self.edit_nvalue_porosity, 0, 1, 1, 1)
        self.button_nvalue_porosity = QtGui.QPushButton(self.groupBox_3)
        self.button_nvalue_porosity.setObjectName(_fromUtf8("button_nvalue_porosity"))
        self.gridLayout_4.addWidget(self.button_nvalue_porosity, 0, 2, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.groupBox_10)
        spacerItem = QtGui.QSpacerItem(142, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout.setItem(0, QtGui.QFormLayout.FieldRole, spacerItem)
        self.groupBox_11 = QtGui.QGroupBox(MeshTools)
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_11)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.button_gen_mtr_selected = QtGui.QPushButton(self.groupBox_11)
        self.button_gen_mtr_selected.setObjectName(_fromUtf8("button_gen_mtr_selected"))
        self.verticalLayout.addWidget(self.button_gen_mtr_selected)
        self.button_gen_mtr_all = QtGui.QPushButton(self.groupBox_11)
        self.button_gen_mtr_all.setObjectName(_fromUtf8("button_gen_mtr_all"))
        self.verticalLayout.addWidget(self.button_gen_mtr_all)
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.groupBox_11)
        spacerItem1 = QtGui.QSpacerItem(20, 363, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtGui.QFormLayout.LabelRole, spacerItem1)

        self.retranslateUi(MeshTools)
        QtCore.QMetaObject.connectSlotsByName(MeshTools)

    def retranslateUi(self, MeshTools):
        MeshTools.setWindowTitle(_translate("MeshTools", "Form", None))
        self.groupBox_10.setTitle(_translate("MeshTools", "Operation with group of mesh elements", None))
        self.groupBox.setTitle(_translate("MeshTools", "Hydraulic Conductivity", None))
        self.label_9.setText(_translate("MeshTools", "Multiply Hydraulic Conductivity by:", None))
        self.button_multiply_conduct.setText(_translate("MeshTools", "OK", None))
        self.label_10.setText(_translate("MeshTools", "Set Hydraulict Conductivity X to:", None))
        self.button_nvalue_conduct.setText(_translate("MeshTools", "OK", None))
        self.edit_nvalue_conduct_y.setToolTip(_translate("MeshTools", "<html><head/><body><p>This aplies only for material type 33</p></body></html>", None))
        self.edit_nvalue_conduct_z.setToolTip(_translate("MeshTools", "<html><head/><body><p>This aplies only for material type 33</p></body></html>", None))
        self.label.setText(_translate("MeshTools", "Set Hydraulict Conductivity Y to:", None))
        self.label_2.setText(_translate("MeshTools", "Set Hydraulict Conductivity Z to:", None))
        self.groupBox_2.setTitle(_translate("MeshTools", "Storativity", None))
        self.label_12.setText(_translate("MeshTools", "Set Storativity to:", None))
        self.button_nvalue_storativity.setText(_translate("MeshTools", "OK", None))
        self.groupBox_3.setTitle(_translate("MeshTools", "Porosity", None))
        self.label_14.setText(_translate("MeshTools", "Set Porosity to:", None))
        self.button_nvalue_porosity.setText(_translate("MeshTools", "OK", None))
        self.groupBox_11.setTitle(_translate("MeshTools", "Generate unique material for each element", None))
        self.button_gen_mtr_selected.setText(_translate("MeshTools", "in Mesh List (selected)", None))
        self.button_gen_mtr_all.setText(_translate("MeshTools", "in Mesh File (all)", None))

