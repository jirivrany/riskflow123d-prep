# coding: utf-8
'''
Class representing materials in flow .mtr file
'''

__author__ = "albert"
__date__ = "$10.8.2011 13:37:40$"


import re
import sys


ORDER_OF_MTR = (
 'Materials',
 'Storativity',
 'Geometry',
 'Sorption',
 'SorptionFraction',
 'DualPorosity',
 'Reactions'
 )

FILE_HEAD = '''$MaterialFormat
1.0  0  8
$EndMaterialFormat
'''



class EmptyListException(BaseException):
    '''
    Exception for Empty List
    '''
    pass

class Material(dict):
    '''
    Class representing materials in flow .mtr file
    '''
    def __init__(self):
        super(Material, self).__init__()
        self['type'] = 0
        self['type_spec'] = 0.0
        self['storativity'] = 0.0
        self['sorption'] = 0.0
        self['dualporosity'] = 0.0
        self['sorptionfraction'] = 0.0
        self['geometry_type'] = None
        self['geometry_spec'] = None
        self['reactions'] = None

class MaterialDict(dict):
    '''
    Material file parser. Open file and creates dictionary where keys
    are id's of materials and items are Material objects.
    
    Values are stored as strings, they are mostly printed and need to be 
    in case of numerical operations
    '''
    def __init__(self, file_name):
        '''open the ini file and creates dictionary with values of interest'''
        super(MaterialDict, self).__init__()
        self.file_name = file_name
        self.attribute_name = False
        
        # parse file and create itself
        self.get_data_from_source()
        
    def get_data_from_source(self):
        '''parses open file line by line'''
        filtr = re.compile(r'\s{1,}')
        try:
            with open(self.file_name, 'r') as mtr_file:
                for line in mtr_file:
                    self.parse(line, filtr)
        except IOError:
            err_code = sys.exc_info()[1]
            print ('Error: %s</p>' % err_code )
        
        finally:
            self.validate_self_data()    
            
    def validate_self_data(self):
        '''
        test if object was created without errors
        raises exception if not
        '''            
        if len(self.values()) == 0:
            raise EmptyListException("Failed to load data from Material file. Check if it's in correct format.")

    def parse(self, line, filtr):
        '''
           search a line for = 
           parses values to collections if succeed
           interested only for items in listOfInterest 
        '''
        try:
            line = line.strip()
            if line.count('$') == 1:
                if (line.count('$End')) == 1:
                    self.attribute_name = False
                else:
                    self.attribute_name = line[1:].lower()
                    
            else:
                line = filtr.sub(';', line)
                if self.attribute_name == 'materials' and line.count(';'):
                    key, mtr_type, mtr_type_spec = line.split(';')
                    if not(self.has_key(key)):
                        new_material = Material()
                        new_material['type'] = mtr_type
                        new_material['type_spec'] = mtr_type_spec
                        self[key] = new_material
                
                elif self.attribute_name == 'geometry' and line.count(';'):
                    key, geometry_type, geometry_spec = line.split(';')
                    self[key]['geometry_type'] = geometry_type
                    self[key]['geometry_spec'] = geometry_spec
                    
                elif(self.attribute_name.count('density') == 0):
                    data = line.split(';')
                    
                    key = data[0]
                    if self.has_key(key) and data[1]:
                        self[key][self.attribute_name] = data[1]
                        
        except ValueError:
            pass

    def create_collections(self):
        '''
        Converts values to several lists of attributes
        Those lists can be easily written as output in flow.mtr format
        '''
        result_data = {
                       'materials' : [],
                       'storativity' : [],
                       'sorption' : [],
                       'dualporosity' : [],
                       'sorptionfraction' : [],
                       'geometry' : [],
                       'reactions' : [],
                       }
        
        for key in sorted(self.keys()):
            wrk_mat = self[key]
            material_string = '%s\t%s\t%s' % \
                (key, wrk_mat['type'], wrk_mat['type_spec'])
    
            result_data['materials'].append(material_string)
        
            if wrk_mat['geometry_type']:    
                geometry_string = '%s\t%s\t%s' % \
                    (key, wrk_mat['geometry_type'], wrk_mat['geometry_spec'])    
                result_data['geometry'].append(geometry_string)
        
            result_data['storativity'].append(wrk_mat['storativity'])
            result_data['sorption'].append( wrk_mat['sorption'])
            result_data['dualporosity'].append( wrk_mat['dualporosity'])
            result_data['sorptionfraction'].append( wrk_mat['sorptionfraction'])
            if wrk_mat['reactions']:
                result_data['reactions'].append( wrk_mat['reactions'])
 
        return result_data

if __name__ == '__main__':
    inpt = '/development/python/rf2/test/data/material/mm.mtr'
    tsss = MaterialDict(inpt)            
       