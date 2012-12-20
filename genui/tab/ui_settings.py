# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Thu Dec 20 12:04:47 2012
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

class Ui_tab_settings(object):
    def setupUi(self, tab_settings):
        tab_settings.setObjectName(_fromUtf8("tab_settings"))
        tab_settings.resize(202, 189)
        self.verticalLayout_2 = QtGui.QVBoxLayout(tab_settings)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_12 = QtGui.QGroupBox(tab_settings)
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        self.gridLayout_12 = QtGui.QGridLayout(self.groupBox_12)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.launcher_check_local = QtGui.QCheckBox(self.groupBox_12)
        self.launcher_check_local.setObjectName(_fromUtf8("launcher_check_local"))
        self.gridLayout_12.addWidget(self.launcher_check_local, 1, 1, 1, 1)
        self.edit_local_launcher = QtGui.QLineEdit(self.groupBox_12)
        self.edit_local_launcher.setObjectName(_fromUtf8("edit_local_launcher"))
        self.gridLayout_12.addWidget(self.edit_local_launcher, 2, 1, 1, 1)
        self.launcher_button_local = QtGui.QToolButton(self.groupBox_12)
        self.launcher_button_local.setObjectName(_fromUtf8("launcher_button_local"))
        self.gridLayout_12.addWidget(self.launcher_button_local, 2, 2, 1, 1)
        self.launcher_check_hydra = QtGui.QCheckBox(self.groupBox_12)
        self.launcher_check_hydra.setObjectName(_fromUtf8("launcher_check_hydra"))
        self.gridLayout_12.addWidget(self.launcher_check_hydra, 3, 1, 1, 1)
        self.edit_cluster_launcher = QtGui.QLineEdit(self.groupBox_12)
        self.edit_cluster_launcher.setObjectName(_fromUtf8("edit_cluster_launcher"))
        self.gridLayout_12.addWidget(self.edit_cluster_launcher, 4, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_12)
        self.buttonBox = QtGui.QDialogButtonBox(tab_settings)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Abort|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.retranslateUi(tab_settings)
        QtCore.QMetaObject.connectSlotsByName(tab_settings)

    def retranslateUi(self, tab_settings):
        self.groupBox_12.setTitle(_translate("tab_settings", "Launcher config", None))
        self.launcher_check_local.setText(_translate("tab_settings", "local flow bin", None))
        self.launcher_button_local.setToolTip(_translate("tab_settings", "pick up local flow bin", None))
        self.launcher_button_local.setText(_translate("tab_settings", "...", None))
        self.launcher_check_hydra.setText(_translate("tab_settings", "cluster", None))

