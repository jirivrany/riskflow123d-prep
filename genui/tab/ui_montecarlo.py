# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'montecarlo.ui'
#
# Created: Fri Apr  4 13:30:04 2014
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

class Ui_MonteCarlo(object):
    def setupUi(self, MonteCarlo):
        MonteCarlo.setObjectName(_fromUtf8("MonteCarlo"))
        MonteCarlo.resize(686, 503)
        self.horizontalLayout = QtGui.QHBoxLayout(MonteCarlo)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_monte_1 = QtGui.QGroupBox(MonteCarlo)
        self.groupBox_monte_1.setMinimumSize(QtCore.QSize(0, 400))
        self.groupBox_monte_1.setMouseTracking(False)
        self.groupBox_monte_1.setObjectName(_fromUtf8("groupBox_monte_1"))
        self.formLayout_4 = QtGui.QFormLayout(self.groupBox_monte_1)
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.label_sens_mult_25 = QtGui.QLabel(self.groupBox_monte_1)
        self.label_sens_mult_25.setObjectName(_fromUtf8("label_sens_mult_25"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_sens_mult_25)
        self.edit_monte_tasks = QtGui.QLineEdit(self.groupBox_monte_1)
        self.edit_monte_tasks.setObjectName(_fromUtf8("edit_monte_tasks"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.edit_monte_tasks)
        self.label_sens_mult_26 = QtGui.QLabel(self.groupBox_monte_1)
        self.label_sens_mult_26.setObjectName(_fromUtf8("label_sens_mult_26"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_sens_mult_26)
        self.edit_monte_sigma = QtGui.QLineEdit(self.groupBox_monte_1)
        self.edit_monte_sigma.setObjectName(_fromUtf8("edit_monte_sigma"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.edit_monte_sigma)
        self.label = QtGui.QLabel(self.groupBox_monte_1)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.groupBox_monte_1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_2)
        self.groupBox_monte_buttons = QtGui.QGroupBox(self.groupBox_monte_1)
        self.groupBox_monte_buttons.setTitle(_fromUtf8(""))
        self.groupBox_monte_buttons.setObjectName(_fromUtf8("groupBox_monte_buttons"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout(self.groupBox_monte_buttons)
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.button_monte_compute = QtGui.QPushButton(self.groupBox_monte_buttons)
        self.button_monte_compute.setObjectName(_fromUtf8("button_monte_compute"))
        self.horizontalLayout_18.addWidget(self.button_monte_compute)
        self.button_monte_save = QtGui.QPushButton(self.groupBox_monte_buttons)
        self.button_monte_save.setObjectName(_fromUtf8("button_monte_save"))
        self.horizontalLayout_18.addWidget(self.button_monte_save)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem)
        self.formLayout_4.setWidget(6, QtGui.QFormLayout.SpanningRole, self.groupBox_monte_buttons)
        self.edit_monte_storativity = QtGui.QLineEdit(self.groupBox_monte_1)
        self.edit_monte_storativity.setObjectName(_fromUtf8("edit_monte_storativity"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.edit_monte_storativity)
        self.edit_monte_porosity = QtGui.QLineEdit(self.groupBox_monte_1)
        self.edit_monte_porosity.setObjectName(_fromUtf8("edit_monte_porosity"))
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.FieldRole, self.edit_monte_porosity)
        self.button_sorption_substances = QtGui.QPushButton(self.groupBox_monte_1)
        self.button_sorption_substances.setObjectName(_fromUtf8("button_sorption_substances"))
        self.formLayout_4.setWidget(5, QtGui.QFormLayout.FieldRole, self.button_sorption_substances)
        self.edit_monte_geomcoef = QtGui.QLineEdit(self.groupBox_monte_1)
        self.edit_monte_geomcoef.setObjectName(_fromUtf8("edit_monte_geomcoef"))
        self.formLayout_4.setWidget(4, QtGui.QFormLayout.FieldRole, self.edit_monte_geomcoef)
        self.label_3 = QtGui.QLabel(self.groupBox_monte_1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_4.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout.addWidget(self.groupBox_monte_1)
        self.groupBox_monte_2 = QtGui.QGroupBox(MonteCarlo)
        self.groupBox_monte_2.setObjectName(_fromUtf8("groupBox_monte_2"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.groupBox_monte_2)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.list_monte_mtr = QtGui.QListWidget(self.groupBox_monte_2)
        self.list_monte_mtr.setObjectName(_fromUtf8("list_monte_mtr"))
        self.verticalLayout_13.addWidget(self.list_monte_mtr)
        self.horizontalLayout.addWidget(self.groupBox_monte_2)

        self.retranslateUi(MonteCarlo)
        QtCore.QMetaObject.connectSlotsByName(MonteCarlo)

    def retranslateUi(self, MonteCarlo):
        MonteCarlo.setWindowTitle(_translate("MonteCarlo", "Form", None))
        self.groupBox_monte_1.setTitle(_translate("MonteCarlo", "Monte Carlo", None))
        self.label_sens_mult_25.setText(_translate("MonteCarlo", "How many tasks?", None))
        self.label_sens_mult_26.setText(_translate("MonteCarlo", "Hydraulic cond. sigma", None))
        self.label.setText(_translate("MonteCarlo", "Storativity", None))
        self.label_2.setText(_translate("MonteCarlo", "Porosity", None))
        self.button_monte_compute.setText(_translate("MonteCarlo", "Compute", None))
        self.button_monte_save.setText(_translate("MonteCarlo", "Generate tasks", None))
        self.button_sorption_substances.setText(_translate("MonteCarlo", "Sorption for substances", None))
        self.edit_monte_geomcoef.setToolTip(_translate("MonteCarlo", "<html><head/><body><p>Sigma for geometry coeficient. Applicable only for 2D elements (type 11, 21, 22).</p></body></html>", None))
        self.label_3.setText(_translate("MonteCarlo", "Geometry coeficient", None))
        self.groupBox_monte_2.setTitle(_translate("MonteCarlo", "List of materials", None))

