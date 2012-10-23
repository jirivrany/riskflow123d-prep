'''
Created on 23.10.2012

@author: Jiri Vrany
'''
import unittest
import os
from app.parser import flow

class Test(unittest.TestCase):


    def testFlow(self):
        fileName = '../../../data/01/flow_t.ini'
        adr = os.path.dirname(fileName)
        print adr
        slovnik = flow.get_dict_from_file(fileName)
        for key,name in slovnik.items():
            fname = adr + os.sep +name
            test = flow.open_file(fname)
            if test:
                print '%s is OK' % key
            else:
                print "failed to open %s file" % key


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testFlow']
    unittest.main()