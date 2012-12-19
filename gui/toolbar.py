'''
Created on 19.12.2012

@author: Jiri Vrany
'''

from PySide.QtGui import QToolBar, QAction, QIcon
from PySide.QtCore import Qt

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
        self.setStatusTip('Quick Start')

        
class SolveAction(QAction):
    '''
    solve action
    '''
    def __init__(self, parent = None):
        super(SolveAction, self).__init__(parent)
        self.setIcon(QIcon('./ico/solve8.png'))
        self.setText('Run Solver')
        self.setShortcut('Ctrl+R')
        self.setStatusTip('Run Solver')

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
        
        