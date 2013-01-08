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
FORM.quick_start()

        
    
def test_monte_carlo():
    FORM.on_action_monte_carlo()
    
    monte_carlo = FORM.centralWidget.tab_montecarlo
    
    
    monte_carlo.edit_monte_tasks.setText('5')
    monte_carlo.edit_monte_sigma.setText('0.2')
    
    li_widget = monte_carlo.list_monte_mtr
    my_item = li_widget.item(4)
    li_widget.setItemSelected(my_item, True)
    my_item2 = li_widget.item(8)
    li_widget.setItemSelected(my_item2, True)
    my_item3 = li_widget.item(5)
    li_widget.setItemSelected(my_item3, True)
    
    
    okWidget = monte_carlo.button_monte_compute
    QTest.mouseClick(okWidget, Qt.LeftButton)
    
    assert monte_carlo.groupBox_monte_buttons.title() == '3 materials in memory'
    
    save_widget = monte_carlo.button_monte_save
    QTest.mouseClick(save_widget, Qt.LeftButton)
    assert FORM.statusBar.currentMessage() == '5 new tasks has been created' 

def test_batch_created():
    '''
    after monte carlo test there has to be file with batch
    '''
    file_name = '/development/python/RF_test_data/test_dir_create/MonteCarlo/submit_all.sh'        
    result = os.path.isfile(file_name)
    assert result == True
    
    file_name = '/development/python/RF_test_data/test_dir_create/MonteCarlo/00/run.bat'
    result = os.path.isfile(file_name)
    assert result == True
    
    file_name = '/development/python/RF_test_data/test_dir_create/MonteCarlo/00/cluster.sh'
    result = os.path.isfile(file_name)
    assert result == True