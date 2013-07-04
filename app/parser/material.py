# coding: utf-8
'''
Class representing materials in flow .mtr file
'''

import re
import sys
import os
import app.helpers.solver_utils as solver_utils


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
        line = line.strip()
        if line.count('$') == 1:
            if (line.count('$End')) == 1:
                self.attribute_name = False
            else:
                self.attribute_name = line[1:].lower()
                
        else:
            line = filtr.sub(';', line)
            if self.attribute_name == 'materials' and line.count(';'):
                self.parse_material(line)
            
            elif self.attribute_name == 'geometry' and line.count(';'):
                key, geometry_type, geometry_spec = line.split(';')
                self[key]['geometry_type'] = geometry_type
                self[key]['geometry_spec'] = geometry_spec
                
            else:
                data = line.split(';')
                
                key = data[0]
                if self.has_key(key) and data[1]:
                    self[key][self.attribute_name] = data[1]
                    
        
    def parse_material(self, line):
        '''
        parses line for materials
        line format is
        material_id mtr_type mtr_type_spec
        type spec depends on type and can be 1-3 values  
        '''
        line_values = line.split(';')
        key = line_values[0]
        if not(self.has_key(key)):
            new_material = Material()
            new_material['type'] = line_values[1]
            new_material['type_spec'] = line_values[2:]
            self[key] = new_material
                

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
                (key, wrk_mat['type'], self.format_type_spec_data(wrk_mat['type_spec']))
            
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
        
        output_file = self.__open_output_file(file_name)
        
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
            
        
            
    def format_type_spec_data(self, type_spec_list):
        '''
        format list to specific text format
        '''
        output = ''
        for ele in type_spec_list:
            output += '{} '.format(ele)
    
        return output.strip()
            
    def __open_output_file(self, file_name):
        '''
        Open output file, create dir if not exists
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
        
        return output_file
                        
    def multiply_property(self, property_name, id_list, multiplicator):
        '''
        multiply defined property for all materials in id_list
        method is used by mesh tools
        '''
        for mtr in id_list:
            if property_name == 'type_spec':
                self.multiply_hydraulic_conductivity(str(mtr), multiplicator)
            else:    
                self.multiply_single_property(str(mtr), property_name, multiplicator)
    
    def multiply_single_property(self, mtr_id, property_name, multiplicator): 
        '''
        multiply one single property used for storativity and porosity
        
        '''
        x_val = self[mtr_id]
        temp = float(x_val[property_name]) * float(multiplicator)
        x_val[property_name] = solver_utils.normalize_result_stora_poro(temp)
        return x_val[property_name]
    
    def multiply_hydraulic_conductivity(self, mtr_id, multiplicator): 
        '''
        multiply hydraulic conductivity
        this value is stored as list (vector) so it has to be formated separately
        '''
        x_val = self[mtr_id]
        x_val['type_spec'] = [float(value) * float(multiplicator) for value in x_val['type_spec']]
        return x_val['type_spec']
    
    def set_hydraulic_conductivity(self, mtr_id, new_value): 
        '''
        multiply hydraulic conductivity
        this value is stored as list (vector) so it has to be formated separately
        '''
        
        x_val = self[mtr_id]
        
        if x_val['type'] == '33':
            x_val['type_spec'] = new_value
        elif x_val['type'] == '22':
            x_val['type_spec'] = new_value[:2]    
        else:
            x_val['type_spec'] = new_value[:1]
            
        return x_val['type_spec']             
            
    def set_property_value(self, property_name, id_list, new_value):
        '''
        set defined property to new value for all materials in id_list
        method is used by mesh tools
        '''
        for mtr in id_list:
            if property_name == 'type_spec':
                self.set_hydraulic_conductivity(str(mtr), new_value)
            else:    
                self.set_single_property_value(str(mtr), property_name, new_value)
            
    def set_single_property_value(self,  mtr_id, property_name, new_value):
        '''
        set defined property to new value 
        method is used by mesh tools
        common method for storativity and dual porosity
        '''
        new_value = solver_utils.normalize_result_stora_poro(new_value)
        self[mtr_id][property_name] = str(new_value)
        return str(new_value)    
    
    def compute_new_material_values(self, mtr_id, values_row):
        '''
        values row is tuple created in sensitivity task or monte carlo
        (conductivity, porosity, storativity)
        '''
        new_cond = None
        new_poro = None
        new_stora = None
        
        
        #conductivity
        if values_row[0]:
            new_cond = self.multiply_hydraulic_conductivity(mtr_id, values_row[0])
        #porosity
        if values_row[1]:
            new_poro = self.set_single_property_value(mtr_id, 'dualporosity', values_row[1])
        #storativity
        if values_row[2]:
            new_stora = self.multiply_single_property(mtr_id, 'storativity', values_row[2])
            
        return (new_cond, new_poro, new_stora)
    
if __name__ == '__main__':
    inpt = '/home/albert/riskflow_test_data/rf2_test/material/mtr_v5_10_2.mtr'
    #ff = open(inpt)
    TEST_MAT = MaterialDict(inpt)
    print TEST_MAT.values() 
    
    inpt2 = '/home/albert/riskflow_test_data/rf2_test/material/mm.mtr'
    #ff = open(inpt)
    TEST_MAT2 = MaterialDict(inpt2)
    print TEST_MAT2.values()   
        