'''
Created on 11.10.2012

@author: albert
'''
import os
from genericpath import exists
from app.helpers.constants import SEPARATOR

DIRNAME = {'monte' : 'MonteCarlo', 'sens' : 'Sensitivity', 'basic' : 'basicProblem'}

        
def set_output_dir(start_dir, method, separator = SEPARATOR):
    '''
    output dir string builder
    '''
    output_dir = start_dir + separator + DIRNAME[method] + separator
    return output_dir

def exist(output_dir):
    '''
    simple alias for generic path command
    '''
    return exists(output_dir)
    
def create(output_dir):
    '''
    if output dir not exsist create it
    if it's not empty display warning
    '''
        
    try:
        os.mkdir(output_dir)
    except OSError:
        print "Failed to create {}".format(output_dir)
        return False
    else:       
        return "Output directory {} created".format(output_dir)


def is_not_empty(output_dir):
    '''
    Is output dir empty?
    '''
    if os.listdir(output_dir) != []: 
        return True
    else:
        return False
    
def get_max_dir_number(output_dir):
    '''
    find maximum number of dir / dir names are numbers
    '''
    return int(max(os.listdir(output_dir), key = to_int))
        
    
def delete_content(output_dir):
    '''
    delete content of output dir
    '''    
    import shutil
    try:
        shutil.rmtree(output_dir)
        create(output_dir)
    except WindowsError:
        print "Can not delete the {} dir - it's used by another process".format(output_dir)         

def to_int(value):
    try:
        return int(value)
    except ValueError:
        pass        
