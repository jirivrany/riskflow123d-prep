'''
Created on 21.12.2012

@author: Jiri Vrany
'''
import copy
from app.Settings import SEPARATOR
from os.path import isfile


def copy_unchanged_files(output_dir, flow_ini_file_name):
    '''
    copy original files to output dir 
    '''
    fname = output_dir + SEPARATOR + 'flow.ini'
    if not isfile(fname):
        work_copy = copy.copy(flow_ini_file_name)
        new_output = open(fname, 'w')
        print >> new_output, work_copy
        new_output.close()
        
        self.create_master_task('')
    finally:
        mtr_file = self.output_dir + '/' + self.file_dict['Material']
        msh_file = self.output_dir + '/' + self.file_dict['Mesh']
        
        self.save_material_file(mtr_file)
        self.msh.write(msh_file)
        self.create_launcher_scripts(fname)
        
        self.save_mtr_button.setDisabled(1)
        self.messenger('All changes saved to output dir', 8000)
