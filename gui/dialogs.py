'''
Created on 30.1.2013

@author: Jiri Vrany
'''
from PyQt4.QtGui import QMessageBox, QPushButton

def empty_output_dir(parent, output_dir):
    '''
    dialog if output dir content can be deleted
    '''
    
    message = "Output dir {} is not empty. Clean up it's content?".format(output_dir)
    ret = QMessageBox.question(parent, 'Directory is not empty', message,
            QMessageBox.Ok, QMessageBox.Cancel)
    
    
    if ret == QMessageBox.Ok:
        return True
    else:
        return False
    
def append_or_empty_output_dir(parent, output_dir):
    '''
    dialog if output dir content can be deleted or has to be appended
    '''
    
    message_box = QMessageBox()
    message_box.setWindowTitle('Directory is not empty')
    message_box.setText("Directory {} is not empty. Clean or append it's content?".format(output_dir))
    button_clean   = QPushButton('Clean it')
    message_box.addButton(button_clean, QMessageBox.YesRole)
    button_cancel   = QPushButton('Cancel')
    message_box.addButton(button_cancel, QMessageBox.NoRole)
    button_append   = QPushButton('Append')
    message_box.addButton(button_append, QMessageBox.ActionRole)
    ret = message_box.exec_();
    return ret