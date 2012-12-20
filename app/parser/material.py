# coding: utf-8
'''
Class representing materials in flow .mtr file
'''

import re
import sys
import os


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
                    
                else:
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
        simple_keys = ('storativity', 'sorption', 'dualporosity', 'sorptionfraction', 'reactions')
        
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
            
            for material_property in simple_keys:
                if wrk_mat[material_property] is not None:
                    temp_string = '{}\t{}'.format(key, wrk_mat[material_property])
                    result_data[material_property].append(temp_string)
 
        return result_data
    
    def save_changes(self, file_name):
        '''
        Save values in flow.mtr format to file_name
        '''
        try:
            output_file = open(file_name,'w')
        except IOError:
            adr = os.path.dirname(file_name)
            try: 
                os.mkdir(adr)
                output_file = open(file_name,'w')
            except IOError:    
                print 'Error: file %s did not exists. Failed to create dir %s' % (file_name, adr)
                return
        
        data_to_save = self.create_collections()
        
        output_file.write(FILE_HEAD)
        
        for material_property in ORDER_OF_MTR:
            output_file.write('${}\n'.format(material_property))
            key = material_property.lower()
            if material_property == 'Materials':
                output_file.write(str(len(data_to_save['materials'])) + '\n')
            
            for line in data_to_save[key]:
                output_file.write(line)
                output_file.write('\n')
            output_file.write('$End{}\n'.format(material_property))
                        

    