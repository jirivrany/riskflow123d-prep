from PyQt4.QtCore import QRegExp
from PyQt4.QtGui import QRegExpValidator

class MyZeroOneValidator(QRegExpValidator):
    
    '''
    Fix for strange behavior of default QDoubleValidator
    '''

    def __init__(self, parent = None):
        
        regex = QRegExp("0{0,}\.{0,1}\d+")
        
        super(MyZeroOneValidator, self).__init__(regex, parent)
        