# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sensitivity.ui'
#
# Created: Thu Jan 24 09:57:37 2013
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
        self.edit_sens_conduct_2 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_conduct_2.setObjectName(_fromUtf8("edit_sens_conduct_2"))
        self.gridLayout.addWidget(self.edit_sens_conduct_2, 4, 1, 1, 1)
        self.label_sens_mult_2 = QtGui.QLabel(self.groupBox_sens_1)
        self.label_sens_mult_2.setObjectName(_fromUtf8("label_sens_mult_2"))
        self.gridLayout.addWidget(self.label_sens_mult_2, 4, 0, 1, 1)
        self.edit_sens_conduct_3 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_conduct_3.setObjectName(_fromUtf8("edit_sens_conduct_3"))
        self.gridLayout.addWidget(self.edit_sens_conduct_3, 5, 1, 1, 1)
        self.label_sens_mult_5 = QtGui.QLabel(self.groupBox_sens_1)
        self.label_sens_mult_5.setObjectName(_fromUtf8("label_sens_mult_5"))
        self.gridLayout.addWidget(self.label_sens_mult_5, 7, 0, 1, 1)
        self.label_sens_mult_6 = QtGui.QLabel(self.groupBox_sens_1)
        self.label_sens_mult_6.setObjectName(_fromUtf8("label_sens_mult_6"))
        self.gridLayout.addWidget(self.label_sens_mult_6, 8, 0, 1, 1)
        self.edit_sens_conduct_5 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_conduct_5.setObjectName(_fromUtf8("edit_sens_conduct_5"))
        self.gridLayout.addWidget(self.edit_sens_conduct_5, 7, 1, 1, 1)
        self.label_sens_mult_3 = QtGui.QLabel(self.groupBox_sens_1)
        self.label_sens_mult_3.setObjectName(_fromUtf8("label_sens_mult_3"))
        self.gridLayout.addWidget(self.label_sens_mult_3, 5, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_sens_1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.edit_sens_storativity_8 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_storativity_8.setObjectName(_fromUtf8("edit_sens_storativity_8"))
        self.gridLayout.addWidget(self.edit_sens_storativity_8, 10, 4, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_sens_1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)
        self.edit_sens_porosity_6 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_porosity_6.setObjectName(_fromUtf8("edit_sens_porosity_6"))
        self.gridLayout.addWidget(self.edit_sens_porosity_6, 8, 2, 1, 1)
        self.edit_sens_porosity_5 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_porosity_5.setObjectName(_fromUtf8("edit_sens_porosity_5"))
        self.gridLayout.addWidget(self.edit_sens_porosity_5, 7, 2, 1, 1)
        self.edit_sens_porosity_3 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_porosity_3.setObjectName(_fromUtf8("edit_sens_porosity_3"))
        self.gridLayout.addWidget(self.edit_sens_porosity_3, 5, 2, 1, 1)
        self.edit_sens_storativity_1 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_storativity_1.setObjectName(_fromUtf8("edit_sens_storativity_1"))
        self.gridLayout.addWidget(self.edit_sens_storativity_1, 2, 4, 1, 1)
        self.edit_sens_porosity_7 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_porosity_7.setObjectName(_fromUtf8("edit_sens_porosity_7"))
        self.gridLayout.addWidget(self.edit_sens_porosity_7, 9, 2, 1, 1)
        self.edit_sens_porosity_8 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_porosity_8.setObjectName(_fromUtf8("edit_sens_porosity_8"))
        self.gridLayout.addWidget(self.edit_sens_porosity_8, 10, 2, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_sens_1)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.edit_sens_storativity_2 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_storativity_2.setObjectName(_fromUtf8("edit_sens_storativity_2"))
        self.gridLayout.addWidget(self.edit_sens_storativity_2, 4, 4, 1, 1)
        self.edit_sens_conduct_1 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_conduct_1.setObjectName(_fromUtf8("edit_sens_conduct_1"))
        self.gridLayout.addWidget(self.edit_sens_conduct_1, 2, 1, 1, 1)
        self.label_sens_mult_4 = QtGui.QLabel(self.groupBox_sens_1)
        self.label_sens_mult_4.setObjectName(_fromUtf8("label_sens_mult_4"))
        self.gridLayout.addWidget(self.label_sens_mult_4, 6, 0, 1, 1)
        self.edit_sens_conduct_4 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_conduct_4.setObjectName(_fromUtf8("edit_sens_conduct_4"))
        self.gridLayout.addWidget(self.edit_sens_conduct_4, 6, 1, 1, 1)
        self.edit_sens_conduct_6 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_conduct_6.setObjectName(_fromUtf8("edit_sens_conduct_6"))
        self.gridLayout.addWidget(self.edit_sens_conduct_6, 8, 1, 1, 1)
        self.label_sens_mult_7 = QtGui.QLabel(self.groupBox_sens_1)
        self.label_sens_mult_7.setObjectName(_fromUtf8("label_sens_mult_7"))
        self.gridLayout.addWidget(self.label_sens_mult_7, 9, 0, 1, 1)
        self.edit_sens_conduct_7 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_conduct_7.setObjectName(_fromUtf8("edit_sens_conduct_7"))
        self.gridLayout.addWidget(self.edit_sens_conduct_7, 9, 1, 1, 1)
        self.label_sens_mult_8 = QtGui.QLabel(self.groupBox_sens_1)
        self.label_sens_mult_8.setObjectName(_fromUtf8("label_sens_mult_8"))
        self.gridLayout.addWidget(self.label_sens_mult_8, 10, 0, 1, 1)
        self.edit_sens_conduct_8 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_conduct_8.setObjectName(_fromUtf8("edit_sens_conduct_8"))
        self.gridLayout.addWidget(self.edit_sens_conduct_8, 10, 1, 1, 1)
        self.edit_sens_porosity_4 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_porosity_4.setObjectName(_fromUtf8("edit_sens_porosity_4"))
        self.gridLayout.addWidget(self.edit_sens_porosity_4, 6, 2, 1, 1)
        self.edit_sens_storativity_3 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_storativity_3.setObjectName(_fromUtf8("edit_sens_storativity_3"))
        self.gridLayout.addWidget(self.edit_sens_storativity_3, 5, 4, 1, 1)
        self.edit_sens_storativity_4 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_storativity_4.setObjectName(_fromUtf8("edit_sens_storativity_4"))
        self.gridLayout.addWidget(self.edit_sens_storativity_4, 6, 4, 1, 1)
        self.edit_sens_storativity_5 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_storativity_5.setObjectName(_fromUtf8("edit_sens_storativity_5"))
        self.gridLayout.addWidget(self.edit_sens_storativity_5, 7, 4, 1, 1)
        self.edit_sens_storativity_6 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_storativity_6.setObjectName(_fromUtf8("edit_sens_storativity_6"))
        self.gridLayout.addWidget(self.edit_sens_storativity_6, 8, 4, 1, 1)
        self.edit_sens_storativity_7 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_storativity_7.setObjectName(_fromUtf8("edit_sens_storativity_7"))
        self.gridLayout.addWidget(self.edit_sens_storativity_7, 9, 4, 1, 1)
        self.edit_sens_porosity_2 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_porosity_2.setObjectName(_fromUtf8("edit_sens_porosity_2"))
        self.gridLayout.addWidget(self.edit_sens_porosity_2, 4, 2, 1, 1)
        self.edit_sens_porosity_1 = QtGui.QLineEdit(self.groupBox_sens_1)
        self.edit_sens_porosity_1.setObjectName(_fromUtf8("edit_sens_porosity_1"))
        self.gridLayout.addWidget(self.edit_sens_porosity_1, 2, 2, 1, 1)
        self.label_sens_mult_1 = QtGui.QLabel(self.groupBox_sens_1)
        self.label_sens_mult_1.setObjectName(_fromUtf8("label_sens_mult_1"))
        self.gridLayout.addWidget(self.label_sens_mult_1, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_sens_1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
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
        self.groupBox_sens_1.setTitle(_translate("Sensitivity", "Choose multiplicator for material property", None))
        self.label_sens_mult_2.setText(_translate("Sensitivity", "<html><head/><body><p align=\"center\">#2</p></body></html>", None))
        self.label_sens_mult_5.setText(_translate("Sensitivity", "<html><head/><body><p align=\"center\">#5</p></body></html>", None))
        self.label_sens_mult_6.setText(_translate("Sensitivity", "<html><head/><body><p align=\"center\">#6</p></body></html>", None))
        self.label_sens_mult_3.setText(_translate("Sensitivity", "<html><head/><body><p align=\"center\">#3</p></body></html>", None))
        self.label_3.setText(_translate("Sensitivity", "Porosity", None))
        self.label_2.setText(_translate("Sensitivity", "Storativity", None))
        self.label.setText(_translate("Sensitivity", "Conductivity", None))
        self.label_sens_mult_4.setText(_translate("Sensitivity", "<html><head/><body><p align=\"center\">#4</p></body></html>", None))
        self.label_sens_mult_7.setText(_translate("Sensitivity", "<html><head/><body><p align=\"center\">#7</p></body></html>", None))
        self.label_sens_mult_8.setText(_translate("Sensitivity", "<html><head/><body><p align=\"center\">#8</p></body></html>", None))
        self.label_sens_mult_1.setText(_translate("Sensitivity", "Multiplicator", None))
        self.label_4.setText(_translate("Sensitivity", "<html><head/><body><p align=\"center\">#1</p></body></html>", None))
        self.button_sens_cross.setText(_translate("Sensitivity", "multiplicator x Material ", None))
        self.button_sens_group.setText(_translate("Sensitivity", "multiplicator x Group of materials", None))
        self.groupBox_sens_2.setTitle(_translate("Sensitivity", "List of materials", None))

