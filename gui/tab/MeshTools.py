# -*- coding: utf-8 -*-

'''
@author: Jiri Vrany

RiskFlow 123D
Tab widget for Mesh Tools
'''

from genui.tab.ui_mesh_tools import Ui_MeshTools
from PyQt4.QtGui import QWidget


from gui.MyDoubleValidator import MyDoubleValidator
from gui.MyZeroOneValidator import MyZeroOneValidator

import copy



class MeshToolsTab(QWidget, Ui_MeshTools):
    '''
    Tab widget for Mesh Tools
    '''
    #alias for settings object
    
    
    def __init__(self, parent = None):
        super(MeshToolsTab, self).__init__(parent)
        self.setupUi(self)
        self.__set_validators()
        
        self.button_multiply_conduct.clicked.connect(self.multiply_hydraulic_conductivity)
        
        self.button_nvalue_conduct.clicked.connect(self.set_hydraulic_conductivity)
        self.button_nvalue_porosity.clicked.connect(self.set_dualporosity)
        self.button_nvalue_storativity.clicked.connect(self.set_storativity)
        
        self.button_gen_mtr_selected.clicked.connect(self.generate_um_for_selected)
        self.button_gen_mtr_all.clicked.connect(self.generate_um_for_all)
        
        
        
        #shortening aliases
        self.messenger = self.window().statusBar.showMessage
        self.material = self.window().material_dict
        self.mesh_settings = self.window().centralWidget.tab_mesh_settings
        
    def __set_validators(self):
        '''
        set validators for edit fields
        '''    
        
        
        validator_positive_double = MyDoubleValidator(True, self)
        validator_zero_one = MyZeroOneValidator(self)
        
        
        
        
        self.edit_multiply_conduct.setValidator(validator_positive_double)
        self.edit_nvalue_conduct.setValidator(validator_positive_double)
        self.edit_nvalue_storativity.setValidator(validator_zero_one)
        self.edit_nvalue_porosity.setValidator(validator_zero_one)
        
    def generate_um_for_all(self):
        '''
        simple slot for signal
        generate unique material 
        '''
        lst = self.mesh_settings.msh.elements  
        idx = self.mesh_settings.msh.mtr_index
        self.generate_um_wrapper(lst, idx)    
        
    def generate_um_for_selected(self):
        '''
        simple slot for signal
        generate unique material for selected elements 
        '''
        lst = self.mesh_settings.displayed_mesh_list    
        idx = self.mesh_settings.mtr_index_disp_lst
        self.generate_um_wrapper(lst, idx)
        
    def generate_um_wrapper(self, lst, idx):
        '''
        generates for selected i self.meshDisplayed
        '''
        
        msg = 'Creating %s new materials. It may take a while...' % str(len(lst))
        self.messenger(msg)
        
        self.generate_uniqe_material(lst, idx)
        
        self.window().centralWidget.tab_material.fill_material_form()
        self.mesh_settings.mesh_list_refresh()
        self.mesh_settings.fill_mesh_mtr_form()
        
        msg = '%s new materials has been created' % str(len(lst))
        self.messenger(msg, 8000)
        #self.save_mtr_button.setEnabled(True)    
        
    def generate_uniqe_material(self, elms, idx):
        '''
        parses the elements dict and generates new material using mtr_index
        '''    
        for mat, elem in idx.items():
            poc = len(str(mat))
            counter = 1
            for el_nr in elem:
                name_string = str(mat)+'{num:0{width}}'.format(num=counter, width=poc+1)
                counter += 1
                #modify structures
                elms[el_nr][1][0] = int(name_string) #mesh
                
                #and material
                new_material = copy.copy(self.material[str(mat)])
                new_material.id = int(name_string)
                self.material[name_string] = new_material
           
            del self.mesh_settings.msh.mtr_index[mat] #material was replaced by new set    
        
    def multiply_hydraulic_conductivity(self):
        '''
        take value from the form, take mtr from list of mesh if any, and multiply
        '''
        mul = self.edit_multiply_conduct.text()
        
        mats = set([d[1][0] for d in self.mesh_settings.displayed_mesh_list.values()])
        
        self.material.multiply_property('type_spec', mats, mul)
        
        self.window().centralWidget.tab_material.fill_material_form()
        msg = '%s Materials has been updated' % len(mats)
        self.messenger(msg)
                
    def set_hydraulic_conductivity(self):
        '''sets the new value of hydraulic conductivity for selected elements'''
        new_value = self.edit_nvalue_conduct.text()
        self.__set_property('type_spec', new_value)
        
    def set_storativity(self):
        '''sets the new value of storativity for selected elements'''
        new_value = self.edit_nvalue_storativity.text()
        self.__set_property('storativity', new_value)
        
    def set_dualporosity(self):
        '''sets the new value of dualporosity for selected elements'''
        new_value = self.edit_nvalue_porosity.text()
        self.__set_property('dualporosity', new_value)    
        
    def __set_property(self, property_name, new_value):
        '''sets the new value of defined property for selected elements'''
        mats = set([d[1][0] for d in self.mesh_settings.displayed_mesh_list.values()])
        
        self.material.set_property_value(property_name, mats, new_value)
            
        self.window().centralWidget.tab_material.fill_material_form() 
        msg = '{} of {} materials has been updated'.format(property_name, len(mats))
        self.messenger(msg)            
        