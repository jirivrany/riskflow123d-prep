'''
Created on 23.10.2012

@author: Jiri Vrany
'''

from PyQt4.QtGui import QStatusBar, QFont
from app.helpers.constants import APP_NAME

import datetime

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
        simple logging by print to file
        '''
        file_name = '{}{}.log'.format(log_into, APP_NAME.lower())
        with open(file_name, 'a') as log_file:
            print >> log_file, '{} {}'.format(datetime.datetime.now(), message)
    
    