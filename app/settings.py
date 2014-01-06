'''
Created on 22.10.2012

@author: albert
'''

from os.path import isfile
from iniparse import INIConfig


__inifile__ = './riskFlow123d.ini'


class Settings(object):
    
    def __init__(self, fname = __inifile__):
        '''
        Application settings class
        '''
        self.storage = fname
        self._create_storage_if_not_exists()
        self.values = None
        self.load_settings()
        
    def __str__(self):
        '''
        print setup values
        '''
        return str(self.values)    
        
    def _create_storage_if_not_exists(self):
        '''
        check if storage file exists, create new one if not
        '''
        if not (isfile(self.storage)):
            setup = "[Output]\nDir = ''\n[Launcher]\nLocal = True\nLocal_bin = \nCluster = False\nCluster_bin = /share/apps/flow123d/bin/flow123d\n[Work]\nLast = ''\n"  
            new_ini_file = open(self.storage, 'w')
            print >> new_ini_file, setup
            new_ini_file.close()
            
    def load_settings(self):
        '''
        load data from storage file and create setup object
        '''
        try:
            ftload = open(self.storage,'r')
        except IOError:
            print "failed to open ini file"
        finally:                
            self.values = INIConfig(ftload)
            ftload.close()
        
    def save_settings(self):
        '''
        save app setup
        '''
        setup_file = open(self.storage, 'w')
        print >> setup_file, self.values
        setup_file.close()