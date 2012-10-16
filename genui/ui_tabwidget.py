# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabwidget.ui'
#
# Created: Tue Oct 16 15:06:30 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(400, 300)

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(QtGui.QApplication.translate("TabWidget", "TabWidget", None, QtGui.QApplication.UnicodeUTF8))

