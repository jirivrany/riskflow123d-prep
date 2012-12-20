# -*- coding: utf-8 -*-

'''
@author: Jiri Vrany

Application Settings Tab
'''

from genui.tab.ui_material import Ui_tab_material
from PyQt4.QtGui import QWidget, QIntValidator, QDoubleValidator


class MaterialTab(QWidget, Ui_tab_material):
    '''
    Settings Tab Widget Material with generated UI
    '''
    def __init__(self, parent = None):
        super(MaterialTab, self).__init__(parent)
        self.setupUi(self)
        
        self.selector_material.activated.connect(self.get_material_from_dict)
        self.button_cancel_mtr_edit.clicked.connect(self.get_material_from_dict)
       
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
        self.get_material_from_dict() #fill up the form for first node
        
    def get_material_from_dict(self):
        '''in selector is id of material, try to get it and fill up the form'''
        idx = self.selector_material.currentText()
        
        try:
            material = self.window().material_dict[idx]
        except KeyError:
            self.window().statusBar.showMessage(\
                'ERROR - no such material : {}'.format(idx), 8000)
        else:
            #type and type spec (conductivity)
            self.edit_type.setText(material['type'])
            self.edit_specific_data.setText(material['type_spec'][0])
            #geometry
            self.edit_geometry_type.setDisabled(True)
            if material['type'] == '21':
                self.edit_geometry_coeficient.setEnabled(True)
                self.edit_geometry_type.setText(material['geometry'][0])
                self.edit_geometry_coeficient.setText(material['geometry'][1])
            else:
                self.edit_geometry_coeficient.setDisabled(True)
            #storativity
            self.edit_storativity.setText(material['storativity'][0])
            #dual porosity
            self.editl_dual_porosity.setText(material['dualporosity'][0])     
        
    def __set_validators(self):
        '''
        set validators for edit fields
        '''    
        
        validator_positive_integer = QIntValidator()
        validator_positive_integer.setBottom(0)
        
        validator_positive_double = QDoubleValidator()
        validator_positive_double.setBottom(0.0)
        
        self.edit_specific_data.setValidator(validator_positive_double)
        self.edit_geometry_coeficient.setValidator(validator_positive_double)
        self.edit_geometry_type.setValidator(validator_positive_integer)
        self.edit_storativity.setValidator(validator_positive_double)
        self.editl_dual_porosity.setValidator(validator_positive_double)
        self.edit_type.setValidator(validator_positive_integer)