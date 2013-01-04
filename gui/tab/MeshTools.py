# -*- coding: utf-8 -*-

'''
@author: Jiri Vrany

RiskFlow 123D
Tab widget for Mesh Tools
'''

from genui.tab.ui_mesh_tools import Ui_MeshTools
from PyQt4.QtGui import QWidget

import copy



class MeshToolsTab(QWidget, Ui_MeshTools):
    '''
    Tab widget for Mesh Tools
    '''
    #alias for settings object
    
    
    def __init__(self, parent = None):
        super(MeshToolsTab, self).__init__(parent)
        self.setupUi(self)
        
        self.button_multiply_conduct.clicked.connect(self.multiply_hydraulic_conductivity)
        self.button_nvalue_conduct.clicked.connect(self.set_hydraulic_conductivity)
        self.button_gen_mtr_selected.clicked.connect(self.generate_um_for_selected)
        self.button_gen_mtr_all.clicked.connect(self.generate_um_for_all)
        
        #shortening aliases
        self.messenger = self.window().statusBar.showMessage
        self.material = self.window().material_dict
        self.mesh_settings = self.window().centralWidget.tab_mesh_settings
        
    def generate_um_for_all(self):
        '''
        simple slot for signal
        generate unique material 
        '''
        self.generate_um_wrapper('all')    
        
    def generate_um_for_selected(self):
        '''
        simple slot for signal
        generate unique material for selected elements 
        '''
        self.generate_um_wrapper('list')
        
    def generate_um_wrapper(self, target = 'all'):
        '''
        generates for selected i self.meshDisplayed
        '''
        if target == 'all':
            lst = self.mesh_settings.msh.elements  
            idx = self.mesh_settings.msh.mtr_index
        elif target == 'list':
            lst = self.mesh_settings.displayed_mesh_list    
            idx = self.mesh_settings.mtr_index_disp_lst
        else:
            return False
        
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
        mats = set([d[1][0] for d in self.displayed_mesh_list.values()])
        for mtr in mats:
            x_val = self.material_dict[str(mtr)]
            temp = float(x_val.type_spec) * float(mul)
            x_val.type_spec = str(temp)
            
        self.fill_mtr_form()    
        msg = '%s Materials has been updated' % len(mats)
        self.messenger(msg)
        self.tabWidget.setCurrentIndex(3)
        self.save_mtr_button.setEnabled(True)         
                
    def set_hydraulic_conductivity(self):
        '''sets the new value of hydraulic conductivity of selected elements'''
        mul = self.edit_nvalue_conduct.text()
        mats = set([d[1][0] for d in self.displayed_mesh_list.values()])
        for mtr in mats:
            temp = self.material_dict[str(mtr)]
            temp.type_spec = str(mul)
            
        self.fill_mtr_form()    
        msg = '%s Materials has been updated' % len(mats)
        self.messenger(msg)
        self.tabWidget.setCurrentIndex(3)
        self.save_mtr_button.setEnabled(True)   
        