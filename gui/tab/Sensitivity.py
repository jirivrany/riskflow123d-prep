# -*- coding: utf-8 -*-

'''
@author: Jiri Vrany

RiskFlow 123D
Tab widget for Mesh Tools
'''

from genui.tab.ui_sensitivity import Ui_Sensitivity
from PyQt4.QtGui import QWidget, QListWidgetItem, QAbstractItemView

from gui.validators import MyDoubleValidator, MyZeroOneValidator
from app.helpers.constants import SEPARATOR
from app.helpers import batch
from app.helpers import solver_utils

from gui.dialogs.SensitivityDialog import SensitivityDialog
import copy

class SensitivityTab(QWidget, Ui_Sensitivity):
    '''
    Tab widget for Mesh Tools
    @todo validatr for number of lines
    '''
    def __init__(self, parent = None):
        super(SensitivityTab, self).__init__(parent)
        self.setupUi(self)
        self.button_sens_cross.clicked.connect(self.make_sens_multiplication)
        self.button_sens_group.clicked.connect(self.make_sens_multiplication_group)
        self.button_sens_lines_dialog.clicked.connect(self.sensitivity_dialog)
        #substances
        self.substances = False
        self.check_substances()
        
        #multipleseclect
        self.list_sens_mtr.setSelectionMode(QAbstractItemView.MultiSelection)
        #alias
        self.messenger = self.window().statusBar.showMessage
        self.material = self.window().material_dict
        #launchers 
        self.local_launcher, self.cluster_launcher = self.window().get_launchers()
        #init count (for append names)
        self.initial_count = 0
        #fill solver list with materials
        self.displayed_solver_mtr_list = [ ]
        data = sorted(self.material.keys())
        self.fill_solver_mtr_list(data)
        #dict for sorption
        self.sorption_values = {}
        self.editor_values = {}
        self.number_of_multipliers = 1
        
    def sensitivity_dialog(self):
        '''
        dialog for multipliers
        '''
        self.check_number_of_multipliers()
            
        dlg = SensitivityDialog(self.number_of_multipliers, self, self.substances)
        if dlg.exec_():
            self.editor_values = dlg.get_values()
            if self.substances:
                self.sorption_values = dlg.sorption_values
                
    def check_number_of_multipliers(self):
        '''
        check how many multipliers we will be using
        '''
        try:
            lines = int(self.edit_sens_num_lines.text())
        except ValueError:
            lines = 1
                
        if lines > 1:
            self.number_of_multipliers = lines            
            
    def check_substances(self):
        '''
        check if substances are present 
        '''
        #buttons for dialog
        if self.window().flow_ini.substances['Sorption'] == 'Yes':
            self.substances = self.window().flow_ini.substances 
                    
        
    def set_initial_count(self, value):
        '''
        setter for inital count
        value has to be type int, or it can be True and in that case we need
        to make it zero
        '''
        
        if type(value) == int:
            self.initial_count = value
        else:
            self.initial_count = 0
        
        
        
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
        
        count = self.initial_count
        
        for material_id in selection:
            for row_nr in range(self.number_of_multipliers): 
                key = str(row_nr)
                
                values_row, sorption_values = self.__get_values_for_current_material(key, self.editor_values)
                
                if values_row or sorption_values:
                    workcopy = copy.deepcopy(self.material)
                    count += 1
                    fdir = '{num:0{width}}'.format(num=count, width=poc+1)
                    #operation with material
                    mtr_file = self.window().output_dir + fdir +\
                    SEPARATOR + self.window().flow_ini.dict_files['Material']
                    if values_row:
                        changed_values = workcopy.compute_new_material_values(material_id, values_row)
                    if sorption_values:
                        workcopy.compute_new_sorption_val(material_id, sorption_values)
                        
                    workcopy.save_changes(mtr_file)
                    self.create_common_task_files(fdir)
                    
                    if values_row:
                        message = '{} computed values {} (None = no change)\n'.format(material_id, changed_values)
                        self.log_message(message, fdir)
                    
                    workcopy = {}    
        
        if self.window().centralWidget.tab_settings.launcher_check_hydra.isChecked():
            batch.create_cluster_batch(self.window().output_dir)
        
        self.message_after_computation(count)
        
    def __get_values_for_current_material(self, key, field_values):
        '''
        search key in dicts
        '''
        try:
            values_row = field_values[key]
        except KeyError:
            values_row = None
        
        try:
            sorption_values = self.sorption_values[key]
        except KeyError:
            sorption_values = None    
            
        return values_row, sorption_values    
                        
    
    
    def make_sens_multiplication_group(self):
        '''
        takes all multiplicators  (A) from the form and selected materials
        from list (B). Computes A results for Group B of materials and creates new tasks
        '''
        self.window().create_master_task() 
           
        selection, pocet = self.get_selected_items()
        
        
        if not selection:
            msg = "Select some material first"        
            self.messenger(msg)
            return
        
        #field_values = self.get_editor_values()
        count = self.initial_count
        
        for row_nr in range(self.number_of_multipliers): 
            key = str(row_nr)
            values_row, sorption_values = self.__get_values_for_current_material(key, self.editor_values)
            if values_row or sorption_values:
                workcopy = copy.deepcopy(self.material)
                count += 1
                message = 'Log for sensitivity changes (conductvity, prorosity, storativity). (None = no change)\n'
                for material_id in selection:
                    if values_row:
                        changed_values = workcopy.compute_new_material_values(material_id, values_row)
                        message += '{} new values {} \n'.format(material_id, changed_values)
                    if sorption_values:
                        workcopy.compute_new_sorption_val(material_id, sorption_values)
                    
                fdir = '{num:0{width}}'.format(num=count, width=pocet+1)
                fname = self.window().output_dir + fdir + SEPARATOR + self.window().flow_ini.dict_files['Material'] 
                
                workcopy.save_changes(fname)
                
                self.create_common_task_files(fdir)
                
                self.log_message(message, fdir)
                    
                workcopy = {}    
        
        if self.window().centralWidget.tab_settings.launcher_check_hydra.isChecked():
            batch.create_cluster_batch(self.window().output_dir)
        
        self.message_after_computation(count)
         
        
    def message_after_computation(self, count):
        '''
        display a message after computation
        '''
        if self.initial_count > 0:    
            msg = "{} new tasks has been appended to existing directory".format(count - self.initial_count)
        else:
            msg = "{} new tasks has been created".format(count)               
        self.messenger(msg)   
            
        
    
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