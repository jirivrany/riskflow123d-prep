'''
Created on 30.1.2013

@author: Jiri Vrany
'''
from PyQt4.QtGui import QMessageBox

def empty_output_dir(parent, output_dir):
    
    message = "Output dir {} is not empty. Clean up it's content?".format(output_dir)
    ret = QMessageBox.question(parent, 'Question Message', message,
            QMessageBox.Ok, QMessageBox.Cancel)
    
    
    if ret == QMessageBox.Ok:
        print "mazeme"
    else:
        print "aaaaa"    
    return str(ret)