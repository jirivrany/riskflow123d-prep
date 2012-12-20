'''
Created on 23.10.2012

@author: Jiri Vrany
'''

from PyQt4.QtGui import QStatusBar, QFont


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
    
        