# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created: Thu Dec 20 12:03:30 2012
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

class Ui_menuBar(object):
    def setupUi(self, menuBar):
        menuBar.setObjectName(_fromUtf8("menuBar"))
        menuBar.resize(680, 21)
        self.menu_Ini_File = QtGui.QMenu(menuBar)
        self.menu_Ini_File.setObjectName(_fromUtf8("menu_Ini_File"))
        self.menuSo_lve = QtGui.QMenu(menuBar)
        self.menuSo_lve.setObjectName(_fromUtf8("menuSo_lve"))
        self.menuTools = QtGui.QMenu(menuBar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.actionOpen = QtGui.QAction(menuBar)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionClose = QtGui.QAction(menuBar)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionSave = QtGui.QAction(menuBar)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionExit = QtGui.QAction(menuBar)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionBasic_Problem = QtGui.QAction(menuBar)
        self.actionBasic_Problem.setObjectName(_fromUtf8("actionBasic_Problem"))
        self.actionMonte_Carlo = QtGui.QAction(menuBar)
        self.actionMonte_Carlo.setObjectName(_fromUtf8("actionMonte_Carlo"))
        self.actionSensitivy_task = QtGui.QAction(menuBar)
        self.actionSensitivy_task.setObjectName(_fromUtf8("actionSensitivy_task"))
        self.actionQuick_start = QtGui.QAction(menuBar)
        self.actionQuick_start.setObjectName(_fromUtf8("actionQuick_start"))
        self.actionSave_Material = QtGui.QAction(menuBar)
        self.actionSave_Material.setObjectName(_fromUtf8("actionSave_Material"))
        self.menu_Ini_File.addSeparator()
        self.menu_Ini_File.addAction(self.actionOpen)
        self.menu_Ini_File.addAction(self.actionClose)
        self.menu_Ini_File.addAction(self.actionSave)
        self.menu_Ini_File.addSeparator()
        self.menu_Ini_File.addAction(self.actionExit)
        self.menuSo_lve.addAction(self.actionBasic_Problem)
        self.menuSo_lve.addAction(self.actionMonte_Carlo)
        self.menuSo_lve.addAction(self.actionSensitivy_task)
        self.menuTools.addAction(self.actionQuick_start)
        self.menuTools.addAction(self.actionSave_Material)
        menuBar.addAction(self.menu_Ini_File.menuAction())
        menuBar.addAction(self.menuSo_lve.menuAction())
        menuBar.addAction(self.menuTools.menuAction())

        self.retranslateUi(menuBar)
        QtCore.QMetaObject.connectSlotsByName(menuBar)

    def retranslateUi(self, menuBar):
        self.menu_Ini_File.setTitle(_translate("menuBar", "&Ini File", None))
        self.menuSo_lve.setTitle(_translate("menuBar", "So&lve", None))
        self.menuTools.setTitle(_translate("menuBar", "Tools", None))
        self.actionOpen.setText(_translate("menuBar", "Open", None))
        self.actionClose.setText(_translate("menuBar", "Close", None))
        self.actionSave.setText(_translate("menuBar", "Save", None))
        self.actionExit.setText(_translate("menuBar", "Exit", None))
        self.actionBasic_Problem.setText(_translate("menuBar", "Basic Problem", None))
        self.actionMonte_Carlo.setText(_translate("menuBar", "Monte Carlo", None))
        self.actionSensitivy_task.setText(_translate("menuBar", "Sensitivy task", None))
        self.actionQuick_start.setText(_translate("menuBar", "Quick start", None))
        self.actionSave_Material.setText(_translate("menuBar", "Save Material", None))

