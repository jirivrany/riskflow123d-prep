'''
Created on 23.10.2012

@author: Jiri Vrany
'''
import unittest
import os
import app.parser.flow as parser
from app.Settings import SEPARATOR

class Test(unittest.TestCase):

    def setUp(self):
        self.fileName = 'data/flow_t.ini'
        self.slovnik = parser.get_dict_from_file(self.fileName)
    
    def test_flow(self):
        
        adr = os.path.dirname(self.fileName)
        vzor = [True, True, True, True, False, True, True]
        result = []
        
        for key,name in self.slovnik.items():
            fname = adr + os.sep +name
            test = parser.open_file(fname)
            if test:
                result.append(True)
            else:
                result.append(False)

        self.assertListEqual(vzor, result, 'chyba testu na kontrolu cteni flow.ini')

    def test_short_check(self):
        '''
        kratky test pouze pro inputy / pouziva se pri testovani v RiskFlow pro FlowCheck
        ''' 
        ini_dir = 'data'
        vzor = [True, True, True, True]
        result = []

        for key, name in parser.EXTENSIONS_DICT['Input'].iteritems():
                
                temp_name = ini_dir + SEPARATOR + self.slovnik[key]
                test = os.path.isfile(temp_name)
                result.append(test)

        self.assertListEqual(vzor, result, 'chyba testu cteni vstupnich souboru flow.ini')        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testFlow']
    unittest.main()
    