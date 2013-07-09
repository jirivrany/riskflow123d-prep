# -*- coding: utf-8 -*-

'''
@author: Jiri Vrany

Application Settings Tab
'''

from genui.tab.ui_material import Ui_tab_material
from PyQt4.QtGui import QWidget, QIntValidator
from gui.MyDoubleValidator import MyDoubleValidator
from gui.MyZeroOneValidator import MyZeroOneValidator

from app.helpers import solver_utils


class MaterialTab(QWidget, Ui_tab_material):
    '''
    Settings Tab Widget Material with generated UI
    '''
    def __init__(self, parent = None):
        super(MaterialTab, self).__init__(parent)
        self.setupUi(self)
        
        self.selector_material.activated.connect(self.get_current_index)
        self.button_cancel_mtr_edit.clicked.connect(self.get_current_index)
        self.button_save_mtr_mem.clicked.connect(self.set_material_to_dict)
       
        self.__set_validators()
        
        self.fill_material_form()
        
    def fill_material_form(self):
        '''
        fill the material editor tab
        with values from application MaterialDict
        '''
        self.selector_material.clear()
        
        material = self.window().material_dict
        
        data = sorted(material.keys())
        #self.displayed_mtr_list = data[:]
        self.selector_material.insertItems(0, data)
        self.get_current_index() #fill up the form for first node
        
    def get_current_index(self):    
        '''
        get current selected index
        '''
        idx = str(self.selector_material.currentText())
        self.get_material_from_dict(idx)
        
    def get_material_from_dict(self, idx):
        '''in selector is id of material, try to get it and fill up the form'''
        try:
            material = self.window().material_dict[idx]
        except KeyError:
            self.window().statusBar.showMessage(\
                'ERROR - no such material : {}'.format(idx), 8000)
        else:
            #type and type spec (conductivity)
            self.edit_type.setText(material['type'])
            self.fill_form_material_type_spec(material)
            #geometry
            self.edit_geometry_type.setDisabled(True)
            if material['type'] == '21':
                self.edit_geometry_coeficient.setEnabled(True)
                self.edit_geometry_type.setText(material['geometry_type'])
                self.edit_geometry_coeficient.setText(material['geometry_spec'])
            else:
                self.edit_geometry_coeficient.setDisabled(True)
            #storativity
            self.edit_storativity.setText(material['storativity'])
            #dual porosity
            self.editl_dual_porosity.setText(material['dualporosity'])
            
    def fill_form_material_type_spec(self, material):
        '''
        Some materials can have conductivity in more than one direction
        Material['type_spec'] is a list and number of elements in this list is the
        number of directions.
        '''
        self.edit_specific_data_1.hide()
        self.edit_specific_data_1.clear()
        self.edit_specific_data_2.hide()
        self.edit_specific_data_2.clear()
        
        self.label_hydrcon_1.hide()
        self.label_hydrcon_2.hide()
        
        for axis, value in enumerate(material['type_spec']):
            row_name = 'edit_specific_data_{}'.format(axis)
            label_name = 'label_hydrcon_{}'.format(axis)
            getattr(self, row_name).setText(value)
            getattr(self, row_name).show()
            getattr(self, label_name).show()
            
            
    def set_material_to_dict(self):
        '''
           in selector is index of material
           try to get current form values and update data in memory 
        '''
        idx = str(self.selector_material.currentText())
        try:
            material_object = self.window().material_dict[idx]
            material_object['type_spec'] = self.material_specific_val_to_list()
            material_object['geometry_type'] = str(self.edit_geometry_type.text())
            material_object['geometry_spec'] = str(self.edit_geometry_coeficient.text())
            material_object['storativity'] = solver_utils.round_storativity_porosity(self.edit_storativity.text())
            material_object['dualporosity'] = solver_utils.round_storativity_porosity(self.editl_dual_porosity.text())
            
        except KeyError:
            self.window().statusBar.showMessage('ERROR no save', 2000)
       
        self.window().statusBar.showMessage('MTR changes saved to Memory', 2000)
    
    def material_specific_val_to_list(self):
        '''
            hydraulic conductivity can have more than one direction 
            get it from form and set it to dict in a list
        '''
        new_value = [str(self.edit_specific_data_0.text()),
                   str(self.edit_specific_data_1.text()),
                   str(self.edit_specific_data_2.text())]
        
        new_value = [old for old in new_value if old is not '']
        
        return new_value
    
        
    def __set_validators(self):
        '''
        set validators for edit fields
        '''    
        
        validator_positive_integer = QIntValidator()
        validator_positive_integer.setBottom(0)
        
        validator_positive_double = MyDoubleValidator(True, self)
        validator_zero_one = MyZeroOneValidator(self)
        
        self.edit_specific_data_0.setValidator(validator_positive_double)
        self.edit_specific_data_1.setValidator(validator_positive_double)
        self.edit_specific_data_2.setValidator(validator_positive_double)
        self.edit_geometry_coeficient.setValidator(validator_positive_double)
        self.edit_geometry_type.setValidator(validator_positive_integer)
        self.edit_storativity.setValidator(validator_zero_one)
        self.editl_dual_porosity.setValidator(validator_zero_one)
        self.edit_type.setValidator(validator_positive_integer)