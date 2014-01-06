'''
Created on 22.10.2012

@author: albert
'''

from app.parser import flow
from os import path

class FlowIni(object):
    '''
    A flow Ini file object
    '''


    def __init__(self, fname):
        '''
        Constructor
        @param fname - name of inifile
        '''
        self.file_name = fname
        self.dir_name = path.split(fname)[0]
        self.dict_files = flow.get_dict_from_file(fname)
        self.substances = flow.get_substances_from_file(fname)
        self.text = flow.get_txt_from_file(fname)
        
    def get_material_file_name(self):
        '''
        material file name
        '''
        return self.dir_name + path.sep + self.dict_files['Material']
    
    def get_mesh_file_name(self):
        '''
        mesh file name
        '''
        return self.dir_name + path.sep + self.dict_files['Mesh']
    
    def create_changed_copy(self, new_file_name, **kvargs):
        '''accepts list of changes
          @param fname: file name to save   
        '''
        opened_file = flow.open_file(self.file_name)
        working_copy = flow.parser(opened_file)
        
        for dkeys in flow.EXTENSIONS_DICT.keys():
            for iner_keys in flow.EXTENSIONS_DICT[dkeys].keys():
                if iner_keys != 'Transport_out':
                    working_copy[dkeys][iner_keys] = '../master/' + self.dict_files[iner_keys]
        
        for key in kvargs:
            working_copy['Input'][key] = kvargs[key]
        
        new_ini_file = open(new_file_name, 'w')
        print >> new_ini_file, working_copy
        new_ini_file.close()