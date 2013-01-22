# -*- coding: utf-8 -*-

'''
@author: Jiri Vrany

RiskFlow 123D
Tab widget for Mesh Tools
'''

from genui.tab.ui_sensitivity import Ui_Sensitivity
from PyQt4.QtGui import QWidget, QListWidgetItem, QAbstractItemView

from app.helpers.constants import SEPARATOR
from app.helpers import batch
from app.helpers import solver_utils


import copy

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
        
        #alias
        self.messenger = self.window().statusBar.showMessage
        self.material = self.window().material_dict
        
        #launchers 
        self.local_launcher, self.cluster_launcher = self.window().get_launchers()
        
        
        #fill solver list with materials
        self.displayed_solver_mtr_list = [ ]
        data = sorted(self.material.keys())
        self.fill_solver_mtr_list(data)
        
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
        count = 0
        
        for mat in selection:
            for i in range(1, 9):
                workcopy = copy.deepcopy(self.material)
                editor_field_value = getattr(self, "edit_sens_mult_{}".format(i)).text()
                if editor_field_value != '':
                    count += 1
                    fdir = '{num:0{width}}'.format(num=count, width=poc+1)
                    #operation with material
                    mtr_file = self.window().output_dir + fdir +\
                     SEPARATOR + self.window().flow_ini.dict_files['Material']
                    nval = float(workcopy[mat]['type_spec']) * float(editor_field_value)
                    workcopy[mat].type_spec = nval
                    workcopy.save_changes(mtr_file)
                    
                    self.create_common_task_files(fdir)
                    
                    message = '{} {} {}'.format(mat, workcopy[mat].type_spec, nval)
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
           
        selection, poc = self.get_selected_items()
        count = 0
        
        for i in xrange(1, 9):
            workcopy = copy.deepcopy(self.material)
            editor_field_values = getattr(self, "edit_sens_mult_{}".format(i)).text()
            if editor_field_values != '':
                count += 1
                message = ''
                for mat in selection:
                    nval = float(workcopy[mat]['type_spec']) * float(editor_field_values)
                    message += '{} {} {}\n'.format(mat, workcopy[mat]['type_spec'], nval)
                    workcopy[mat].type_spec = nval
                    
                fdir = '{num:0{width}}'.format(num=count, width=poc+1)
                fname = self.window().output_dir + fdir + SEPARATOR + self.window().flow_ini.dict_files['Material'] 
                
                workcopy.save_changes(fname)
                
                self.create_common_task_files(fdir)
                
                self.log_message(message, fdir)
                
                
            workcopy = {}    
        
        if self.window().centralWidget.tab_settings.launcher_check_hydra.isChecked():
            batch.create_cluster_batch(self.window().output_dir)
            
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