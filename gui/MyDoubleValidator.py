from PyQt4.QtCore import QRegExp
from PyQt4.QtGui import QRegExpValidator


class MyDoubleValidator(QRegExpValidator):

    '''
    Fix for strange behavior of default QDoubleValidator
    '''

    def __init__(self, positive=True, parent=None):

        if positive:
            regex = QRegExp("\d+\.{0,1}\d{0,}")
        else:
            regex = QRegExp("-{0,1}\d+\.{0,1}\d{0,}")

        super(MyDoubleValidator, self).__init__(regex, parent)
