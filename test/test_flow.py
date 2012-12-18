'''
Created on 23.10.2012

@author: Jiri Vrany
'''
import os
import app.parser.flow as parser
from app.Settings import SEPARATOR

file_name = 'data/flow_t.ini'
slovnik = parser.get_dict_from_file(file_name)
    
def test_flow():
    
    adr = os.path.dirname(file_name)
    vzor = [True, True, True, True, False, True, True]
    result = []
    
    for name in slovnik.itervalues():
        fname = adr + os.sep +name
        test = parser.open_file(fname)
        if test:
            result.append(True)
        else:
            result.append(False)

    assert vzor == result

def test_short_check():
    '''
    kratky test pouze pro inputy / pouziva se pri testovani v RiskFlow pro FlowCheck
    ''' 
    ini_dir = 'data'
    vzor = [True, True, True, True]
    result = []

    for key in parser.EXTENSIONS_DICT['Input'].iterkeys():
            
            temp_name = ini_dir + SEPARATOR + slovnik[key]
            test = os.path.isfile(temp_name)
            result.append(test)

    assert vzor == result        


