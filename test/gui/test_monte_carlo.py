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

MOCK_INI = '/home/albert/riskflow_test_data/test_dir_create/flow_t.ini'

FORM.start_main_routine(MOCK_INI)

        
    
def test_monte_carlo():
    FORM.on_action_monte_carlo()
    
    monte_carlo = FORM.centralWidget.tab_montecarlo
    
    
    monte_carlo.edit_monte_tasks.setText('2')
    monte_carlo.edit_monte_sigma.setText('0.2')
    
    li_widget = monte_carlo.list_monte_mtr
    my_item = li_widget.item(1)
    li_widget.setItemSelected(my_item, True)
    my_item2 = li_widget.item(2)
    li_widget.setItemSelected(my_item2, True)
    
    
    
    okWidget = monte_carlo.button_monte_compute
    QTest.mouseClick(okWidget, Qt.LeftButton)
    
    assert monte_carlo.groupBox_monte_buttons.title() == '2 materials in memory'
    
    save_widget = monte_carlo.button_monte_save
    QTest.mouseClick(save_widget, Qt.LeftButton)
    
    file_name = '/home/albert/riskflow_test_data/test_dir_create/MonteCarlo/00/00_ini.ini'
    result = os.path.isfile(file_name)
    assert result == True

def test_batch_created():
    '''
    after monte carlo test there has to be file with batch
    '''
    file_name = '/home/albert/riskflow_test_data/test_dir_create/MonteCarlo/submit_all.sh'        
    result = os.path.isfile(file_name)
    assert result == True
    
    file_name = '/home/albert/riskflow_test_data/test_dir_create/MonteCarlo/00/run.bat'
    result = os.path.isfile(file_name)
    assert result == True
    
    file_name = '/home/albert/riskflow_test_data/test_dir_create/MonteCarlo/00/cluster.sh'
    result = os.path.isfile(file_name)
    assert result == True