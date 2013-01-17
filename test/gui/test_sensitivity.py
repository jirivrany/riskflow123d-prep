'''
Created on 8.1.2013

@author: Jiri Vrany
'''
import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtTest import QTest
from PyQt4.QtCore import Qt

from gui import MainWindow
import os.path


APP = QApplication(sys.argv)
FORM = MainWindow.MainWindow()
MOCK_INI = '/home/albert/riskflow_test_data/test_mock/flow_t.ini'

FORM.start_main_routine(MOCK_INI)

class TestSensitivity():
    
    def test_senstitivity_setup(self):
        FORM.on_action_sensitivity()
        
        sensitivity = FORM.centralWidget.tab_sensitivity
        
        
        sensitivity.edit_sens_mult_1.setText('5')
        sensitivity.edit_sens_mult_2.setText('0.2')
        
        li_widget = sensitivity.list_sens_mtr
        my_item = li_widget.item(1)
        li_widget.setItemSelected(my_item, True)
        
        cross_button = sensitivity.button_sens_cross
        QTest.mouseClick(cross_button, Qt.LeftButton)
        
        file_name = '/home/albert/riskflow_test_data/test_mock/Sensitivity/01'
        result = os.path.isdir(file_name)
        assert result == True
        
        
    def test_batch_created(self):
        '''
        after monte carlo test there has to be file with batch
        '''
        file_name = '/home/albert/riskflow_test_data/test_mock/Sensitivity/submit_all.sh'        
        result = os.path.isfile(file_name)
        assert result == True
    
    def test_master_created(self):
        '''
        after monte carlo test there has to be file with batch
        '''
        file_name = '/home/albert/riskflow_test_data/test_mock/Sensitivity/master'
        result = os.path.isdir(file_name)
        assert result == True
    
    def test_log_created(self):
        '''
        after monte carlo test there has to be file with batch
        '''
        file_name = '/home/albert/riskflow_test_data/test_mock/Sensitivity/01/sens01.log'
        result = os.path.isfile(file_name)
        assert result == True    
        

        
        
    @classmethod
    def teardown_class(self):
        """ 
        remove created dir
        """
        FORM.on_app_exit()
        import shutil
        shutil.rmtree('/home/albert/riskflow_test_data/test_mock/Sensitivity') 
    