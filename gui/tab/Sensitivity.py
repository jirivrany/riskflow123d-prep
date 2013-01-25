# -*- coding: utf-8 -*-

'''
@author: Jiri Vrany

RiskFlow 123D
Tab widget for Mesh Tools
'''

from genui.tab.ui_sensitivity import Ui_Sensitivity
from PyQt4.QtGui import QWidget, QListWidgetItem, QAbstractItemView

from gui.MyDoubleValidator import MyDoubleValidator
from app.helpers.constants import SEPARATOR
from app.helpers import batch
from app.helpers import solver_utils


import copy
from scipy.constants.codata import val

class SensitivityTab(QWidget, Ui_Sensitivity):
    '''
    Tab widget for Mesh Tools
    '''
    def __init__(self, parent = None):
        super(SensitivityTab, self).__init__(parent)
        self.setupUi(self)
        self.button_sens_cross.clicked.connect(self.make_sens_multiplication)
        self.button_sens_group.clicked.connect(self.make_sens_multiplication_group)
        
        #multipleseclect
        self.list_sens_mtr.setSelectionMode(QAbstractItemView.MultiSelection)
        #validator
        self.__set_validators()        
        #alias
        self.messenger = self.window().statusBar.showMessage
        self.material = self.window().material_dict
        
        #launchers 
        self.local_launcher, self.cluster_launcher = self.window().get_launchers()
        
        
        #fill solver list with materials
        self.displayed_solver_mtr_list = [ ]
        data = sorted(self.material.keys())
        self.fill_solver_mtr_list(data)
        
    def __set_validators(self):
        '''
        set validators for edit fields
        '''    
        
        validator_positive_double = MyDoubleValidator(parent = self)
        validator_zero_one = MyDoubleValidator(0.00001, 0.99999, 5)
        
        for row_number in xrange(1, 9):
            tmp_name = 'edit_sens_conduct_{}'.format(row_number)
            getattr(self, tmp_name).setValidator(validator_positive_double)
            tmp_name = 'edit_sens_storativity_{}'.format(row_number)
            getattr(self, tmp_name).setValidator(validator_positive_double)
            tmp_name = 'edit_sens_porosity_{}'.format(row_number)
            getattr(self, tmp_name).setValidator(validator_zero_one)
        
    def fill_solver_mtr_list(self, data):
        '''
        get the mtr list from dict and fill up the list
        '''    
        
        self.list_sens_mtr.clear()
        self.displayed_solver_mtr_list = data    
        
        for key in data:
            #update of list
            QListWidgetItem(str(key), self.list_sens_mtr)
            
        self.list_sens_mtr.repaint()
        msg = "{0} materials in the list".format(len(data))
        self.groupBox_sens_2.setTitle(msg)
         
        
    def make_sens_multiplication(self):
        '''takes all multiplicators  (A) from the form and selected materials
        from list (B). Computes A x B results and creates new tasks
        '''
        
        self.window().create_master_task() 
           
        selection, poc = self.get_selected_items()
        
        if not selection:
            msg = "Select some material first"        
            self.messenger(msg)
            return
        
        count = 0
        
        field_values = self.get_editor_values()
        
        for material_id in selection:
            for values_row in field_values: 
                workcopy = copy.deepcopy(self.material)
                count += 1
                fdir = '{num:0{width}}'.format(num=count, width=poc+1)
                #operation with material
                mtr_file = self.window().output_dir + fdir +\
                 SEPARATOR + self.window().flow_ini.dict_files['Material']
                
                changed_values = workcopy.compute_new_material_values(material_id, values_row)
                workcopy.save_changes(mtr_file)
                
                self.create_common_task_files(fdir)
                
                message = '{} computed values {} (None = no change)\n'.format(material_id, changed_values)
                self.log_message(message, fdir)
                
                workcopy = {}    
        
        if self.window().centralWidget.tab_settings.launcher_check_hydra.isChecked():
            batch.create_cluster_batch(self.window().output_dir)
            
        msg = "{} new tasks has been created".format(count)           
        self.messenger(msg)
        
        
    
    
    def make_sens_multiplication_group(self):
        '''takes all multiplicators  (A) from the form and selected materials
        from list (B). Computes A results for Group B of materials and creates new tasks
        '''
        self.window().create_master_task() 
           
        selection, pocet = self.get_selected_items()
        count = 0
        
        if not selection:
            msg = "Select some material first"        
            self.messenger(msg)
            return
        
        field_values = self.get_editor_values()
        
        for values_row in field_values: 
            workcopy = copy.deepcopy(self.material)
            count += 1
            message = 'Log for sensitivity changes (conductvity, prorosity, storativity). (None = no change)\n'
            for material_id in selection:
                changed_values = workcopy.compute_new_material_values(material_id, values_row)
                message += '{} new values {} \n'.format(material_id, changed_values)
                
            fdir = '{num:0{width}}'.format(num=count, width=pocet+1)
            fname = self.window().output_dir + fdir + SEPARATOR + self.window().flow_ini.dict_files['Material'] 
            
            workcopy.save_changes(fname)
            
            self.create_common_task_files(fdir)
            
            self.log_message(message, fdir)
                
                
            workcopy = {}    
        
        if self.window().centralWidget.tab_settings.launcher_check_hydra.isChecked():
            batch.create_cluster_batch(self.window().output_dir)
            
        msg = "{} new tasks has been created".format(count)           
        self.messenger(msg)
        
    def get_editor_values(self):
        '''
        check all the editor and return 8 row list of tuples with editor values
        '''
        result = []
        
        for row in xrange(8):
            try:
                conductivity = float(getattr(self, "edit_sens_conduct_{}".format(row + 1)).text())
            except ValueError:
                conductivity = None                
            
            try:
                porosity = float(getattr(self, "edit_sens_porosity_{}".format(row + 1)).text())
            except ValueError:
                porosity = None
            
            try:            
                storativity = float(getattr(self, "edit_sens_storativity_{}".format(row + 1)).text())
            except ValueError:
                storativity = None
            
            if storativity or porosity or conductivity:
                result.append( (conductivity, porosity, storativity) )
            
        return result 
    
    def get_selected_items(self):
        '''
        get items selected in gui as list of strings
        '''
        selection = [str(list_item.text()) for list_item in self.list_sens_mtr.selectedItems()]
        pocet = len(str(len(selection)*9))
        
        return selection, pocet 
     
    def create_common_task_files(self, dir_name):
        '''
        creates files common for both solution methods
        changed ini file in dir_name
        batch scripts
        task identifier
        '''
        ini_file = self.window().output_dir + dir_name + SEPARATOR + dir_name + '_ini.ini'
        self.window().flow_ini.create_changed_copy(ini_file, Material = \
                                       self.window().flow_ini.dict_files['Material'])
        batch.create_launcher_scripts(ini_file, self.local_launcher, self.cluster_launcher)
        solver_utils.create_task_identifier('basic', self.window().output_dir + dir_name)
                
         
     
    def log_message(self, message, where):
        '''
        simple logger - append message to file
        '''
        task_logfile_name = '{}{}/sens{}.log'.format(self.window().output_dir, where, where)
        
        with open(task_logfile_name, 'a') as logfile:
            print >> logfile, message