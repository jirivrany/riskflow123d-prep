# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Tue Oct 23 12:06:39 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_tab_settings(object):
    def setupUi(self, tab_settings):
        tab_settings.setObjectName("tab_settings")
        tab_settings.resize(202, 189)
        self.verticalLayout_2 = QtGui.QVBoxLayout(tab_settings)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_12 = QtGui.QGroupBox(tab_settings)
        self.groupBox_12.setObjectName("groupBox_12")
        self.gridLayout_12 = QtGui.QGridLayout(self.groupBox_12)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.launcher_check_local = QtGui.QCheckBox(self.groupBox_12)
        self.launcher_check_local.setObjectName("launcher_check_local")
        self.gridLayout_12.addWidget(self.launcher_check_local, 1, 1, 1, 1)
        self.edit_local_launcher = QtGui.QLineEdit(self.groupBox_12)
        self.edit_local_launcher.setObjectName("edit_local_launcher")
        self.gridLayout_12.addWidget(self.edit_local_launcher, 2, 1, 1, 1)
        self.launcher_button_local = QtGui.QToolButton(self.groupBox_12)
        self.launcher_button_local.setObjectName("launcher_button_local")
        self.gridLayout_12.addWidget(self.launcher_button_local, 2, 2, 1, 1)
        self.launcher_check_hydra = QtGui.QCheckBox(self.groupBox_12)
        self.launcher_check_hydra.setObjectName("launcher_check_hydra")
        self.gridLayout_12.addWidget(self.launcher_check_hydra, 3, 1, 1, 1)
        self.edit_cluster_launcher = QtGui.QLineEdit(self.groupBox_12)
        self.edit_cluster_launcher.setObjectName("edit_cluster_launcher")
        self.gridLayout_12.addWidget(self.edit_cluster_launcher, 4, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_12)
        self.buttonBox = QtGui.QDialogButtonBox(tab_settings)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Abort|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.retranslateUi(tab_settings)
        QtCore.QMetaObject.connectSlotsByName(tab_settings)

    def retranslateUi(self, tab_settings):
        self.groupBox_12.setTitle(QtGui.QApplication.translate("tab_settings", "Launcher config", None, QtGui.QApplication.UnicodeUTF8))
        self.launcher_check_local.setText(QtGui.QApplication.translate("tab_settings", "local flow bin", None, QtGui.QApplication.UnicodeUTF8))
        self.launcher_button_local.setToolTip(QtGui.QApplication.translate("tab_settings", "pick up local flow bin", None, QtGui.QApplication.UnicodeUTF8))
        self.launcher_button_local.setText(QtGui.QApplication.translate("tab_settings", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.launcher_check_hydra.setText(QtGui.QApplication.translate("tab_settings", "cluster", None, QtGui.QApplication.UnicodeUTF8))

