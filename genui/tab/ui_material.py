# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'material.ui'
#
# Created: Tue Nov 13 12:51:49 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_material(object):
    def setupUi(self, tab_material):
        tab_material.setObjectName("tab_material")
        tab_material.setEnabled(True)
        tab_material.setGeometry(QtCore.QRect(20, 10, 630, 206))
        self.gridLayout = QtGui.QGridLayout(tab_material)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(tab_material)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.selector_material = QtGui.QComboBox(tab_material)
        self.selector_material.setObjectName("selector_material")
        self.gridLayout.addWidget(self.selector_material, 2, 2, 1, 1)
        self.edit_type = QtGui.QLineEdit(tab_material)
        self.edit_type.setReadOnly(True)
        self.edit_type.setObjectName("edit_type")
        self.gridLayout.addWidget(self.edit_type, 3, 2, 1, 1)
        self.edit_specific_data = QtGui.QLineEdit(tab_material)
        self.edit_specific_data.setObjectName("edit_specific_data")
        self.gridLayout.addWidget(self.edit_specific_data, 4, 2, 1, 1)
        self.label_material = QtGui.QLabel(tab_material)
        self.label_material.setObjectName("label_material")
        self.gridLayout.addWidget(self.label_material, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(tab_material)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 3, 1, 1)
        self.label_3 = QtGui.QLabel(tab_material)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.edit_geometry_type = QtGui.QLineEdit(tab_material)
        self.edit_geometry_type.setObjectName("edit_geometry_type")
        self.gridLayout.addWidget(self.edit_geometry_type, 5, 2, 1, 1)
        self.label_4 = QtGui.QLabel(tab_material)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.edit_geometry_coeficient = QtGui.QLineEdit(tab_material)
        self.edit_geometry_coeficient.setObjectName("edit_geometry_coeficient")
        self.gridLayout.addWidget(self.edit_geometry_coeficient, 6, 2, 1, 1)
        self.box_mtr_control = QtGui.QGroupBox(tab_material)
        self.box_mtr_control.setTitle("")
        self.box_mtr_control.setObjectName("box_mtr_control")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.box_mtr_control)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.button_save_mtr_mem = QtGui.QPushButton(self.box_mtr_control)
        self.button_save_mtr_mem.setObjectName("button_save_mtr_mem")
        self.horizontalLayout_2.addWidget(self.button_save_mtr_mem)
        self.button_cancel_mtr_edit = QtGui.QPushButton(self.box_mtr_control)
        self.button_cancel_mtr_edit.setObjectName("button_cancel_mtr_edit")
        self.horizontalLayout_2.addWidget(self.button_cancel_mtr_edit)
        self.gridLayout.addWidget(self.box_mtr_control, 7, 2, 1, 1)

        self.retranslateUi(tab_material)
        QtCore.QMetaObject.connectSlotsByName(tab_material)

    def retranslateUi(self, tab_material):
        self.label.setText(QtGui.QApplication.translate("material", "material type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_material.setText(QtGui.QApplication.translate("material", "Select material", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("material", "hydraulic conductivity", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("material", "geometry type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("material", "geometry coeficient", None, QtGui.QApplication.UnicodeUTF8))
        self.button_save_mtr_mem.setText(QtGui.QApplication.translate("material", "save", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cancel_mtr_edit.setText(QtGui.QApplication.translate("material", "cancel", None, QtGui.QApplication.UnicodeUTF8))

