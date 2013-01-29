from PyQt4.QtGui import QDoubleValidator, QValidator

from sys import float_info

class MyDoubleValidator(QDoubleValidator):
    
    '''
    Fix for strange behavior of default QDoubleValidator
    '''

    def __init__(self, bottom = float_info.min, \
                 top = float_info.max, \
                 decimals = float_info.dig, parent = None):
        
        super(MyDoubleValidator, self).__init__(bottom, top, decimals, parent)

    def validate(self, input_value, pos):
        
        state, pos = QDoubleValidator.validate(self, input_value, pos)
        
        allowed_start_values = ('.', '0', '0.')
        
        if input_value.isEmpty() or input_value in allowed_start_values:
            return QValidator.Intermediate, pos
        
        if state != QValidator.Acceptable:
            return QValidator.Invalid, pos
        
        return QValidator.Acceptable, pos