# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabwidget.ui'
#
# Created: Thu Dec 20 12:05:13 2012
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

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName(_fromUtf8("TabWidget"))
        TabWidget.resize(400, 300)

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget", None))

