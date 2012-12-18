# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'montecarlo.ui'
#
# Created: Tue Dec 04 18:01:48 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MonteCarlo(object):
    def setupUi(self, MonteCarlo):
        MonteCarlo.setObjectName("MonteCarlo")
        MonteCarlo.resize(686, 503)
        self.horizontalLayout = QtGui.QHBoxLayout(MonteCarlo)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_monte_1 = QtGui.QGroupBox(MonteCarlo)
        self.groupBox_monte_1.setMinimumSize(QtCore.QSize(0, 400))
        self.groupBox_monte_1.setMouseTracking(False)
        self.groupBox_monte_1.setObjectName("groupBox_monte_1")
        self.formLayout_4 = QtGui.QFormLayout(self.groupBox_monte_1)
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_sens_mult_25 = QtGui.QLabel(self.groupBox_monte_1)
        self.label_sens_mult_25.setObjectName("label_sens_mult_25")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_sens_mult_25)
        self.edit_monte_tasks = QtGui.QLineEdit(self.groupBox_monte_1)
        self.edit_monte_tasks.setObjectName("edit_monte_tasks")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.edit_monte_tasks)
        self.label_sens_mult_26 = QtGui.QLabel(self.groupBox_monte_1)
        self.label_sens_mult_26.setObjectName("label_sens_mult_26")
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_sens_mult_26)
        self.edit_monte_sigma = QtGui.QLineEdit(self.groupBox_monte_1)
        self.edit_monte_sigma.setObjectName("edit_monte_sigma")
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.edit_monte_sigma)
        self.groupBox_monte_buttons = QtGui.QGroupBox(self.groupBox_monte_1)
        self.groupBox_monte_buttons.setTitle("")
        self.groupBox_monte_buttons.setObjectName("groupBox_monte_buttons")
        self.horizontalLayout_18 = QtGui.QHBoxLayout(self.groupBox_monte_buttons)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.button_monte_compute = QtGui.QPushButton(self.groupBox_monte_buttons)
        self.button_monte_compute.setObjectName("button_monte_compute")
        self.horizontalLayout_18.addWidget(self.button_monte_compute)
        self.button_monte_save = QtGui.QPushButton(self.groupBox_monte_buttons)
        self.button_monte_save.setObjectName("button_monte_save")
        self.horizontalLayout_18.addWidget(self.button_monte_save)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem)
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.SpanningRole, self.groupBox_monte_buttons)
        self.groupBox_26 = QtGui.QGroupBox(self.groupBox_monte_1)
        self.groupBox_26.setObjectName("groupBox_26")
        self.horizontalLayout_17 = QtGui.QHBoxLayout(self.groupBox_26)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.edit_monte_output_dir = QtGui.QLineEdit(self.groupBox_26)
        self.edit_monte_output_dir.setObjectName("edit_monte_output_dir")
        self.horizontalLayout_17.addWidget(self.edit_monte_output_dir)
        self.tool_sens_output_dir_4 = QtGui.QToolButton(self.groupBox_26)
        self.tool_sens_output_dir_4.setObjectName("tool_sens_output_dir_4")
        self.horizontalLayout_17.addWidget(self.tool_sens_output_dir_4)
        self.formLayout_4.setWidget(4, QtGui.QFormLayout.SpanningRole, self.groupBox_26)
        self.horizontalLayout.addWidget(self.groupBox_monte_1)
        self.groupBox_monte_2 = QtGui.QGroupBox(MonteCarlo)
        self.groupBox_monte_2.setObjectName("groupBox_monte_2")
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.groupBox_monte_2)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.list_monte_mtr = QtGui.QListWidget(self.groupBox_monte_2)
        self.list_monte_mtr.setObjectName("list_monte_mtr")
        self.verticalLayout_13.addWidget(self.list_monte_mtr)
        self.horizontalLayout.addWidget(self.groupBox_monte_2)

        self.retranslateUi(MonteCarlo)
        QtCore.QMetaObject.connectSlotsByName(MonteCarlo)

    def retranslateUi(self, MonteCarlo):
        MonteCarlo.setWindowTitle(QtGui.QApplication.translate("MonteCarlo", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_monte_1.setTitle(QtGui.QApplication.translate("MonteCarlo", "Monte Carlo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_sens_mult_25.setText(QtGui.QApplication.translate("MonteCarlo", "How many tasks?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_sens_mult_26.setText(QtGui.QApplication.translate("MonteCarlo", "Sigma", None, QtGui.QApplication.UnicodeUTF8))
        self.button_monte_compute.setText(QtGui.QApplication.translate("MonteCarlo", "Compute", None, QtGui.QApplication.UnicodeUTF8))
        self.button_monte_save.setText(QtGui.QApplication.translate("MonteCarlo", "Generate tasks", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_26.setTitle(QtGui.QApplication.translate("MonteCarlo", "Output Dir", None, QtGui.QApplication.UnicodeUTF8))
        self.tool_sens_output_dir_4.setText(QtGui.QApplication.translate("MonteCarlo", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_monte_2.setTitle(QtGui.QApplication.translate("MonteCarlo", "List of materials", None, QtGui.QApplication.UnicodeUTF8))

