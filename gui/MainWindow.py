from genui.main_window import Ui_MainWindow
from PySide.QtGui import QMainWindow

from gui.TabWidget import MainTabWidget
from gui.MainMenu import MainMenu

class MainWindow(QMainWindow, Ui_MainWindow):
    '''
    Main App window controller
    '''
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.setCentralWidget(MainTabWidget())
        self.setMenuBar(MainMenu()) 