'''
Created on 20.12.2012

@author: Jiri Vrany
'''
from app.Settings import SEPARATOR
import os
import shutil

def identify_task(problem_type, work_dir):
    '''
    Save problem identifier file into given work_dir
    '''
    try:
        task_file = open(work_dir + '/problem.type', 'w')
        print >> task_file, problem_type
        task_file.close()
    except IOError:
        print 'oh crap'


def copy_master_files(flow_ini, output_dir):
    '''
    create a copy of original basic problem
    @param output_dir - where to copy
    @param flow_ini - a FlowIni object
    '''
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
        
    original_dir = flow_ini.dir_name
        
    for master_file_name in flow_ini.file_names_dict.values():
        src = original_dir + SEPARATOR + master_file_name
        try:
            shutil.copy2(src, output_dir)
        except IOError:
            pass    
  
            