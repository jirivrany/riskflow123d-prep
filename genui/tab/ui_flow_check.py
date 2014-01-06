# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flow_check.ui'
#
# Created: Wed Jan 30 12:29:21 2013
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

class Ui_tab_8(object):
    def setupUi(self, tab_8):
        tab_8.setObjectName(_fromUtf8("tab_8"))
        tab_8.resize(343, 605)
        self.gridLayout_13 = QtGui.QGridLayout(tab_8)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem, 10, 0, 1, 1)
        self.groupBox_editor = QtGui.QGroupBox(tab_8)
        self.groupBox_editor.setObjectName(_fromUtf8("groupBox_editor"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_editor)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.edit_flow_ini = QtGui.QTextEdit(self.groupBox_editor)
        self.edit_flow_ini.setMinimumSize(QtCore.QSize(0, 300))
        self.edit_flow_ini.setObjectName(_fromUtf8("edit_flow_ini"))
        self.verticalLayout_7.addWidget(self.edit_flow_ini)
        self.gridLayout_13.addWidget(self.groupBox_editor, 8, 0, 1, 1)
        self.groupBox_check = QtGui.QGroupBox(tab_8)
        self.groupBox_check.setObjectName(_fromUtf8("groupBox_check"))
        self.gridLayout_14 = QtGui.QGridLayout(self.groupBox_check)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.label_17 = QtGui.QLabel(self.groupBox_check)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_14.addWidget(self.label_17, 0, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.groupBox_check)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_14.addWidget(self.label_18, 0, 1, 1, 1)
        self.title_msh = QtGui.QLabel(self.groupBox_check)
        self.title_msh.setObjectName(_fromUtf8("title_msh"))
        self.gridLayout_14.addWidget(self.title_msh, 2, 0, 1, 1)
        self.label_msh = QtGui.QLabel(self.groupBox_check)
        self.label_msh.setObjectName(_fromUtf8("label_msh"))
        self.gridLayout_14.addWidget(self.label_msh, 2, 1, 1, 1)
        self.title_ngh = QtGui.QLabel(self.groupBox_check)
        self.title_ngh.setObjectName(_fromUtf8("title_ngh"))
        self.gridLayout_14.addWidget(self.title_ngh, 3, 0, 1, 1)
        self.label_ngh = QtGui.QLabel(self.groupBox_check)
        self.label_ngh.setObjectName(_fromUtf8("label_ngh"))
        self.gridLayout_14.addWidget(self.label_ngh, 3, 1, 1, 1)
        self.title_mtr = QtGui.QLabel(self.groupBox_check)
        self.title_mtr.setObjectName(_fromUtf8("title_mtr"))
        self.gridLayout_14.addWidget(self.title_mtr, 4, 0, 1, 1)
        self.label_mtr = QtGui.QLabel(self.groupBox_check)
        self.label_mtr.setObjectName(_fromUtf8("label_mtr"))
        self.gridLayout_14.addWidget(self.label_mtr, 4, 1, 1, 1)
        self.title_bcd = QtGui.QLabel(self.groupBox_check)
        self.title_bcd.setObjectName(_fromUtf8("title_bcd"))
        self.gridLayout_14.addWidget(self.title_bcd, 5, 0, 1, 1)
        self.label_bcd = QtGui.QLabel(self.groupBox_check)
        self.label_bcd.setObjectName(_fromUtf8("label_bcd"))
        self.gridLayout_14.addWidget(self.label_bcd, 5, 1, 1, 1)
        self.lineEdit_bcd = QtGui.QLineEdit(self.groupBox_check)
        self.lineEdit_bcd.setReadOnly(True)
        self.lineEdit_bcd.setObjectName(_fromUtf8("lineEdit_bcd"))
        self.gridLayout_14.addWidget(self.lineEdit_bcd, 5, 3, 1, 1)
        self.lineEdit_mtr = QtGui.QLineEdit(self.groupBox_check)
        self.lineEdit_mtr.setReadOnly(True)
        self.lineEdit_mtr.setObjectName(_fromUtf8("lineEdit_mtr"))
        self.gridLayout_14.addWidget(self.lineEdit_mtr, 4, 3, 1, 1)
        self.lineEdit_ngh = QtGui.QLineEdit(self.groupBox_check)
        self.lineEdit_ngh.setReadOnly(True)
        self.lineEdit_ngh.setObjectName(_fromUtf8("lineEdit_ngh"))
        self.gridLayout_14.addWidget(self.lineEdit_ngh, 3, 3, 1, 1)
        self.lineEdit_msh = QtGui.QLineEdit(self.groupBox_check)
        self.lineEdit_msh.setReadOnly(True)
        self.lineEdit_msh.setObjectName(_fromUtf8("lineEdit_msh"))
        self.gridLayout_14.addWidget(self.lineEdit_msh, 2, 3, 1, 1)
        self.label_25 = QtGui.QLabel(self.groupBox_check)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_14.addWidget(self.label_25, 0, 3, 1, 1)
        self.gridLayout_13.addWidget(self.groupBox_check, 0, 0, 1, 1)

        self.retranslateUi(tab_8)
        QtCore.QMetaObject.connectSlotsByName(tab_8)

    def retranslateUi(self, tab_8):
        self.groupBox_editor.setTitle(_translate("tab_8", "Flow.ini Editor", None))
        self.groupBox_check.setTitle(_translate("tab_8", "Flow.ini Check", None))
        self.label_17.setText(_translate("tab_8", "File Type", None))
        self.label_18.setText(_translate("tab_8", "Status", None))
        self.title_msh.setText(_translate("tab_8", "Elements (.msh)", None))
        self.label_msh.setText(_translate("tab_8", "Fail", None))
        self.title_ngh.setText(_translate("tab_8", "Neighbours (.ngh)", None))
        self.label_ngh.setText(_translate("tab_8", "Fail", None))
        self.title_mtr.setText(_translate("tab_8", "Materials (.mtr)", None))
        self.label_mtr.setText(_translate("tab_8", "Fail", None))
        self.title_bcd.setText(_translate("tab_8", "Boundary cond. (.bcd)", None))
        self.label_bcd.setText(_translate("tab_8", "Fail", None))
        self.label_25.setText(_translate("tab_8", "Given Path (from flow.ini)", None))

