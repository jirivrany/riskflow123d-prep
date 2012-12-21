'''
Created on 11.10.2012

@author: albert
'''
import os
from genericpath import exists

DIRNAME = {'monte' : 'MonteCarlo', 'sens' : 'Sensitivity', 'basic' : 'basicProblem'}

        
def set_output_dir(start_dir, method, separator):
    '''
    output dir string builder
    '''
    output_dir = start_dir + separator + DIRNAME[method] + separator
    return output_dir
    
def create_if_not_exists(output_dir):
    '''
    if output dir not exsist create it
    if it's not empty display warning
    '''
        
    wmsg = 'OK - Empty output dir exists, nothing to do'
    
    if not exists(output_dir):
        try:
            os.mkdir(output_dir)
        except OSError:
            print "Failed to create {}".format(output_dir)
            return False
        else:       
            wmsg = "Output directory {} created".format(output_dir)
            
    elif os.listdir(output_dir) != []: 
        wmsg = 'WARNING: {} is not empty, existing data will be overwritten'.format(output_dir)
        
    return wmsg
        
