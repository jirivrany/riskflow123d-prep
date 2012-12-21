'''
Created on 21.12.2012

@author: Jiri Vrany
'''

def save_material(output_dir, file_name, material, separator = '/'):
    '''
    save material object from memory to new location
    '''
    mtr_file = output_dir + separator + file_name
    
    material.save_changes(mtr_file)
    
    return 'material changes saved to output dir'
