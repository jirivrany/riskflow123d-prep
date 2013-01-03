'''
Created on 23.10.2012

@author: Jiri Vrany
'''

from PyQt4.QtGui import QStatusBar, QFont
from app.helpers import logger
from app.helpers.constants import APP_NAME

class MainStatusBar(QStatusBar):
    '''
    Status Bar for main window
    '''

    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(MainStatusBar, self).__init__(parent)
        self.setFont(QFont("Helvetica [Cronyx]", 12))
        
    
    def showMessage(self, message, msecs = 0, log_into = False):
        '''
        method for showing messages with logging
        if log_into directory is set, then the message is logged into
        app logifle in this directory
        '''
        if log_into:
            self.log_message(message, log_into)
            
        super(MainStatusBar, self).showMessage(message, msecs)

    def log_message(self, message, log_into):
        '''
        get logger and log message
        '''
        my_logger = logger.get_it(APP_NAME, '{}{}.log'.format(log_into, APP_NAME.lower()))
        my_logger.info(message)