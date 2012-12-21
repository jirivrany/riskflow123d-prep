'''
Created on 23.10.2012

@author: Jiri Vrany
'''
import os
import app.parser.flow as parser
from app.Settings import SEPARATOR

print os.getcwd()
    
def test_flow():
    '''
    kompletni nacteni a zpracovani flow ini souboru
    ''' 
    file_name = '/development/python/RF_test_data/rf2_test/flow_t.ini'
    slovnik = parser.get_dict_from_file(file_name)
    
    adr = os.path.dirname(file_name)
    vzor = [True, True, True, True, False, True, True]
    result = []
    
    for name in slovnik.itervalues():
        fname = adr + os.sep +name
        if os.path.isfile(fname):
            result.append(True)
        else:
            result.append(False)

    assert vzor == result

def test_short_check():
    '''
    kratky test pouze pro inputy / pouziva se pri testovani v RiskFlow pro FlowCheck
    ''' 
    file_name = '/development/python/RF_test_data/rf2_test/flow_t.ini'
    slovnik = parser.get_dict_from_file(file_name)
    
    adr = os.path.dirname(file_name)
    vzor = [True, True, True, True]
    result = []

    for key in parser.EXTENSIONS_DICT['Input'].iterkeys():
            
            temp_name = adr + SEPARATOR + slovnik[key]
            test = os.path.isfile(temp_name)
            result.append(test)

    assert vzor == result        


