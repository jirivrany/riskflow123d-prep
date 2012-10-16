# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created: Tue Oct 16 15:58:07 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_menuBar(object):
    def setupUi(self, menuBar):
        menuBar.setObjectName("menuBar")
        menuBar.resize(680, 21)
        self.menu_Ini_File = QtGui.QMenu(menuBar)
        self.menu_Ini_File.setObjectName("menu_Ini_File")
        self.menuSo_lve = QtGui.QMenu(menuBar)
        self.menuSo_lve.setObjectName("menuSo_lve")
        self.menuTools = QtGui.QMenu(menuBar)
        self.menuTools.setObjectName("menuTools")
        self.actionOpen = QtGui.QAction(menuBar)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtGui.QAction(menuBar)
        self.actionClose.setObjectName("actionClose")
        self.actionSave = QtGui.QAction(menuBar)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtGui.QAction(menuBar)
        self.actionExit.setObjectName("actionExit")
        self.actionBasic_Problem = QtGui.QAction(menuBar)
        self.actionBasic_Problem.setObjectName("actionBasic_Problem")
        self.actionMonte_Carlo = QtGui.QAction(menuBar)
        self.actionMonte_Carlo.setObjectName("actionMonte_Carlo")
        self.actionSensitivy_task = QtGui.QAction(menuBar)
        self.actionSensitivy_task.setObjectName("actionSensitivy_task")
        self.actionQuick_start = QtGui.QAction(menuBar)
        self.actionQuick_start.setObjectName("actionQuick_start")
        self.actionSave_Material = QtGui.QAction(menuBar)
        self.actionSave_Material.setObjectName("actionSave_Material")
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
        self.menu_Ini_File.setTitle(QtGui.QApplication.translate("menuBar", "&Ini File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSo_lve.setTitle(QtGui.QApplication.translate("menuBar", "So&lve", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("menuBar", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("menuBar", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("menuBar", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("menuBar", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("menuBar", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBasic_Problem.setText(QtGui.QApplication.translate("menuBar", "Basic Problem", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMonte_Carlo.setText(QtGui.QApplication.translate("menuBar", "Monte Carlo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSensitivy_task.setText(QtGui.QApplication.translate("menuBar", "Sensitivy task", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuick_start.setText(QtGui.QApplication.translate("menuBar", "Quick start", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Material.setText(QtGui.QApplication.translate("menuBar", "Save Material", None, QtGui.QApplication.UnicodeUTF8))

