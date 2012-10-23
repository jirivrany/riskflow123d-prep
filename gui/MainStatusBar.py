'''
Created on 23.10.2012

@author: Jiri Vrany
'''

from PySide.QtGui import QStatusBar, QFont

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
    
    def set_message(self, msg, dis_time=0):
        '''sending messages to status bar, and to log, if it's enabled'''    
        self.showMessage(msg, dis_time)    