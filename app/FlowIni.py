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