'''
Created on 19.12.2012

@author: Jiri Vrany
'''

from PyQt4.QtGui import QToolBar, QAction, QIcon
from PyQt4.QtCore import Qt

class MainToolBar(QToolBar):
    '''
    main toolbar for the window
    '''
    
    def __init__(self, parent = None):
        '''
        Constructor and basic setup
        '''
        super(MainToolBar, self).__init__(parent)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.setMovable(False)
        
class QuickStartAction(QAction):
    '''
    Quick Start 
    '''
    def __init__(self, parent = None):
        super(QuickStartAction, self).__init__(parent)
        self.setIcon(QIcon('./ico/quick8.png'))
        self.setText('Quick Start')
        self.setShortcut('Ctrl+Q')
        
        tip = 'Quick open last working problem.'
        self.setStatusTip(tip)
        self.setToolTip(tip)

        
class SolveAction(QAction):
    '''
    solve action
    '''
    def __init__(self, parent = None):
        super(SolveAction, self).__init__(parent)
        self.setIcon(QIcon('./ico/solve8.png'))
        self.setText('Generate Task')
        self.setShortcut('Ctrl+R')
        
        tip = 'Generate task and save all changes from memory to disk.'
        self.setStatusTip(tip)
        self.setToolTip(tip)

class ExitAction(QAction):
    '''
    exit app
    '''
    def __init__(self, parent = None):
        super(ExitAction, self).__init__(parent)
        self.setIcon(QIcon('./ico/exit8.png'))
        self.setText('Exit')
        self.setShortcut('Ctrl+Q')
        self.setStatusTip('Exit application')
        
        