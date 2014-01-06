# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'material.ui'
#
# Created: Tue Sep 24 12:35:52 2013
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

class Ui_tab_material(object):
    def setupUi(self, tab_material):
        tab_material.setObjectName(_fromUtf8("tab_material"))
        tab_material.setEnabled(True)
        tab_material.resize(630, 375)
        self.gridLayout = QtGui.QGridLayout(tab_material)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 3, 1, 1)
        self.editl_dual_porosity = QtGui.QLineEdit(tab_material)
        self.editl_dual_porosity.setObjectName(_fromUtf8("editl_dual_porosity"))
        self.gridLayout.addWidget(self.editl_dual_porosity, 10, 1, 1, 1)
        self.edit_storativity = QtGui.QLineEdit(tab_material)
        self.edit_storativity.setObjectName(_fromUtf8("edit_storativity"))
        self.gridLayout.addWidget(self.edit_storativity, 9, 1, 1, 1)
        self.edit_specific_data_0 = QtGui.QLineEdit(tab_material)
        self.edit_specific_data_0.setObjectName(_fromUtf8("edit_specific_data_0"))
        self.gridLayout.addWidget(self.edit_specific_data_0, 4, 1, 1, 1)
        self.edit_type = QtGui.QLineEdit(tab_material)
        self.edit_type.setReadOnly(True)
        self.edit_type.setObjectName(_fromUtf8("edit_type"))
        self.gridLayout.addWidget(self.edit_type, 3, 1, 1, 1)
        self.selector_material = QtGui.QComboBox(tab_material)
        self.selector_material.setObjectName(_fromUtf8("selector_material"))
        self.gridLayout.addWidget(self.selector_material, 2, 1, 1, 1)
        self.label = QtGui.QLabel(tab_material)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.label_storativity = QtGui.QLabel(tab_material)
        self.label_storativity.setObjectName(_fromUtf8("label_storativity"))
        self.gridLayout.addWidget(self.label_storativity, 9, 0, 1, 1)
        self.label_dual_porosity = QtGui.QLabel(tab_material)
        self.label_dual_porosity.setObjectName(_fromUtf8("label_dual_porosity"))
        self.gridLayout.addWidget(self.label_dual_porosity, 10, 0, 1, 1)
        self.label_material = QtGui.QLabel(tab_material)
        self.label_material.setObjectName(_fromUtf8("label_material"))
        self.gridLayout.addWidget(self.label_material, 2, 0, 1, 1)
        self.label_hydrcon_0 = QtGui.QLabel(tab_material)
        self.label_hydrcon_0.setObjectName(_fromUtf8("label_hydrcon_0"))
        self.gridLayout.addWidget(self.label_hydrcon_0, 4, 0, 1, 1)
        self.label_3 = QtGui.QLabel(tab_material)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)
        self.edit_geometry_type = QtGui.QLineEdit(tab_material)
        self.edit_geometry_type.setObjectName(_fromUtf8("edit_geometry_type"))
        self.gridLayout.addWidget(self.edit_geometry_type, 7, 1, 1, 1)
        self.label_4 = QtGui.QLabel(tab_material)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 8, 0, 1, 1)
        self.edit_geometry_coeficient = QtGui.QLineEdit(tab_material)
        self.edit_geometry_coeficient.setObjectName(_fromUtf8("edit_geometry_coeficient"))
        self.gridLayout.addWidget(self.edit_geometry_coeficient, 8, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 14, 1, 1, 1)
        self.edit_specific_data_1 = QtGui.QLineEdit(tab_material)
        self.edit_specific_data_1.setObjectName(_fromUtf8("edit_specific_data_1"))
        self.gridLayout.addWidget(self.edit_specific_data_1, 5, 1, 1, 1)
        self.edit_specific_data_2 = QtGui.QLineEdit(tab_material)
        self.edit_specific_data_2.setObjectName(_fromUtf8("edit_specific_data_2"))
        self.gridLayout.addWidget(self.edit_specific_data_2, 6, 1, 1, 1)
        self.label_hydrcon_1 = QtGui.QLabel(tab_material)
        self.label_hydrcon_1.setObjectName(_fromUtf8("label_hydrcon_1"))
        self.gridLayout.addWidget(self.label_hydrcon_1, 5, 0, 1, 1)
        self.label_hydrcon_2 = QtGui.QLabel(tab_material)
        self.label_hydrcon_2.setObjectName(_fromUtf8("label_hydrcon_2"))
        self.gridLayout.addWidget(self.label_hydrcon_2, 6, 0, 1, 1)
        self.button_sorption_substances = QtGui.QPushButton(tab_material)
        self.button_sorption_substances.setObjectName(_fromUtf8("button_sorption_substances"))
        self.gridLayout.addWidget(self.button_sorption_substances, 11, 1, 1, 1)
        self.box_mtr_control = QtGui.QGroupBox(tab_material)
        self.box_mtr_control.setTitle(_fromUtf8(""))
        self.box_mtr_control.setObjectName(_fromUtf8("box_mtr_control"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.box_mtr_control)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.button_save_mtr_mem = QtGui.QPushButton(self.box_mtr_control)
        self.button_save_mtr_mem.setObjectName(_fromUtf8("button_save_mtr_mem"))
        self.horizontalLayout_2.addWidget(self.button_save_mtr_mem)
        self.button_cancel_mtr_edit = QtGui.QPushButton(self.box_mtr_control)
        self.button_cancel_mtr_edit.setObjectName(_fromUtf8("button_cancel_mtr_edit"))
        self.horizontalLayout_2.addWidget(self.button_cancel_mtr_edit)
        self.gridLayout.addWidget(self.box_mtr_control, 12, 1, 1, 1)

        self.retranslateUi(tab_material)
        QtCore.QMetaObject.connectSlotsByName(tab_material)

    def retranslateUi(self, tab_material):
        self.label.setText(_translate("tab_material", "material type", None))
        self.label_storativity.setText(_translate("tab_material", "storativity", None))
        self.label_dual_porosity.setText(_translate("tab_material", "porosity", None))
        self.label_material.setText(_translate("tab_material", "Select material", None))
        self.label_hydrcon_0.setText(_translate("tab_material", "hydraulic conductivity", None))
        self.label_3.setText(_translate("tab_material", "geometry type", None))
        self.label_4.setText(_translate("tab_material", "geometry coeficient", None))
        self.label_hydrcon_1.setText(_translate("tab_material", "hydraulic cond. y", None))
        self.label_hydrcon_2.setText(_translate("tab_material", "hydraulic cond. z", None))
        self.button_sorption_substances.setText(_translate("tab_material", "sorption for substances", None))
        self.button_save_mtr_mem.setText(_translate("tab_material", "save", None))
        self.button_cancel_mtr_edit.setText(_translate("tab_material", "cancel", None))

