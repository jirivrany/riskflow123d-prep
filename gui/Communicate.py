'''
Created on 23.10.2012

@author: Jiri Vrany
'''

from PySide.QtCore import QObject, Signal

class Communicate(QObject):
    # create two new signals on the fly: one will handle
    # int type, the other will handle strings
    send_msg = Signal(str)
    