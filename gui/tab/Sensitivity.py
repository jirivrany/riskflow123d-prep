# -*- coding: utf-8 -*-

'''
@author: Jiri Vrany

RiskFlow 123D
Tab widget for Mesh Tools
'''

from genui.tab.ui_sensitivity import Ui_Sensitivity
from PyQt4.QtGui import QWidget

from app.helpers.constants import SEPARATOR
from app.helpers import batch

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
        self.material_dict = self.window().material_dict
        
        
    def make_sens_multiplication(self):
        '''takes all multiplicators  (A) from the form and selected materials
        from list (B). Computes A x B results and creates new tasks
        '''
        self.create_master_task() 
           
        selection = [a.data(0) for a in self.list_sens_mtr.selectedItems()]
        count = 0
        poc = len(str(len(selection)*9))
        
        for mat in selection:
            for i in range(1, 9):
                workcopy = copy.deepcopy(self.material_dict)
                editor_field_value = getattr(self, "edit_sens_mult_{}".format(i)).text()
                if editor_field_value != '':
                    count += 1
                    fdir = '{num:0{width}}'.format(num=count, width=poc+1)
                    mtr_file = self.output_dir + fdir + SEPARATOR +  self.file_dict['Material']
                    ini_file = self.output_dir + fdir + SEPARATOR + fdir + '_ini.ini'
                    
                    nval = float(workcopy[mat].type_spec) * float(editor_field_value)
                    workcopy[mat].type_spec = nval
                    
                    self.material.saveDictToFile(mtr_file, workcopy)
                    self.create_changed_ini(ini_file, Material = self.file_dict['Material'])
                    self.create_launcher_scripts(ini_file)
                    
                    self.identify_task('basicProblem', self.output_dir + fdir)
                    
                    logfile = open('{}{}/sens{}.log'.format(self.output_dir, fdir, fdir), 'w')
                    print >> logfile, '{} {} {}'.format(mat, workcopy[mat].type_spec, nval)
                    logfile.close()
                    
                workcopy = {}    
        
        if self.launcher_check_hydra.isChecked():
            batch.create_cluster_batch(self.output_dir)
            
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
            workcopy = copy.deepcopy(self.material_dict)
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
     
        