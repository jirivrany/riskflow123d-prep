'''
Created on 8.1.2013

@author: Jiri Vrany
'''
import sys
import unittest
from PyQt4.QtGui import QApplication

from gui import MainWindow


class Test(unittest.TestCase):

    def setUp(self):
        self.app = QApplication(sys.argv)
        self.form = MainWindow.MainWindow()
    
    def test_defaults(self):
        '''Test the GUI in its default state'''
        self.assertEqual(self.form.windowTitle(), 'RiskFlow')
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()