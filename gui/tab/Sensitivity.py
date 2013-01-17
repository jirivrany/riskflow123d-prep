# -*- coding: utf-8 -*-

'''
@author: Jiri Vrany

RiskFlow 123D
Tab widget for Mesh Tools
'''

from genui.tab.ui_sensitivity import Ui_Sensitivity
from PyQt4.QtGui import QWidget, QListWidgetItem

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
        
        #alias
        self.messenger = self.window().statusBar.showMessage
        self.material = self.window().material_dict
        
        #fill solver list with materials
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
           
        selection = [str(list_item.text()) for list_item in self.list_sens_mtr.selectedItems()]
        count = 0
        poc = len(str(len(selection)*9))
        
        local_launcher, cluster_launcher = self.window().get_launchers()
        
        for mat in selection:
            for i in range(1, 9):
                workcopy = copy.deepcopy(self.material)
                editor_field_value = getattr(self, "edit_sens_mult_{}".format(i)).text()
                if editor_field_value != '':
                    count += 1
                    fdir = '{num:0{width}}'.format(num=count, width=poc+1)
                    mtr_file = self.window().output_dir + fdir + SEPARATOR + self.window().flow_ini.dict_files['Material']
                    ini_file = self.window().output_dir + fdir + SEPARATOR + fdir + '_ini.ini'
                    
                    nval = float(workcopy[mat]['type_spec']) * float(editor_field_value)
                    workcopy[mat].type_spec = nval
                    
                    workcopy.save_changes(mtr_file)
                    
                    self.window().flow_ini.create_changed_copy(ini_file, Material = self.window().flow_ini.dict_files['Material'])
            
                    batch.create_launcher_scripts(ini_file, local_launcher, cluster_launcher)
            
                    solver_utils.create_task_identifier('basic', self.window().output_dir + fdir)
                    
                    task_logfile_name = '{}{}/sens{}.log'.format(self.window().output_dir, fdir, fdir)
                    with open(task_logfile_name, 'w') as logfile:
                        print >> logfile, '{} {} {}'.format(mat, workcopy[mat].type_spec, nval)
                    
                workcopy = {}    
        
        if self.window().centralWidget.tab_settings.launcher_check_hydra.isChecked():
            batch.create_cluster_batch(self.window().output_dir)
            
        msg = "{} new tasks has been created".format(count)           
        self.messenger(msg)            
    
    def make_sens_multiplication_group(self):
        '''takes all multiplicators  (A) from the form and selected materials
        from list (B). Computes A results for Group B of materials and creates new tasks
        '''
        self.create_master_task() 
           
        selection = [a.data(0) for a in self.list_sens_mtr.selectedItems()]
        count = 0
        poc = len(str(len(selection)*9))
        
        
        for i in range(1, 9):
            workcopy = copy.deepcopy(self.material)
            editor_field_values = getattr(self, "edit_sens_mult_{}".format(i)).text()
            if editor_field_values != '':
                count += 1
                msz = ''
                for mat in selection:
                    nval = float(workcopy[mat].type_spec) * float(editor_field_values)
                    msz += '{} {} {}\n'.format(mat, workcopy[mat].type_spec, nval)
                    workcopy[mat].type_spec = nval
                    
                fdir = '{num:0{width}}'.format(num=count, width=poc+1)
                fname = self.output_dir + fdir + SEPARATOR +  self.file_dict['Material']
                self.material.saveDictToFile(fname, workcopy)
    
                
                ffname = self.output_dir + fdir + SEPARATOR + fdir + '_ini.ini'
                self.create_changed_ini(ffname, Material = self.file_dict['Material'])
                self.create_launcher_scripts(ffname)
                
                logfile = open('{}{}/sens{}.log'.format(self.output_dir, fdir, fdir), 'w')
                print >> logfile, msz
                logfile.close()
                
            workcopy = {}    
        
        if self.launcher_check_hydra.isChecked():
            batch.create_cluster_batch(self.output_dir)
            
        msg = "{} new tasks has been created".format(count)           
        self.messenger(msg)
     
        