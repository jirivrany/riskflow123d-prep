# -*- coding: utf-8 -*-

'''
@author: Jiri Vrany

RiskFlow 123D
Tab widget for Mesh Tools
'''

from genui.tab.ui_montecarlo import Ui_MonteCarlo
from PyQt4.QtGui import QWidget, QListWidgetItem, QAbstractItemView

from app.helpers import solver_utils
from app.helpers.constants import SEPARATOR

import copy

class MonteCarloTab(QWidget, Ui_MonteCarlo):
    '''
    Tab widget for Mesh Tools
    '''
    def __init__(self, monte_logger, parent = None):
        super(MonteCarloTab, self).__init__(parent)
        self.setupUi(self)
        
        self.displayed_solver_mtr_list = []
        
        self.button_monte_compute.clicked.connect(self.make_monte_carlo)
        self.button_monte_save.clicked.connect(self.save_monte_carlo_results)
        
        self.list_monte_mtr.setSelectionMode(QAbstractItemView.MultiSelection)
        
        self.monte_logger = monte_logger
        
        #dict of distributions for monte carlo method
        self.distributions_dict = {} 
        
        
        #shortening aliases
        self.messenger = self.window().statusBar.showMessage
        self.material = self.window().material_dict
        
        #fill solver list with materials
        data = sorted(self.material.keys())
        self.fill_solver_mtr_list(data)
        
    
    def fill_solver_mtr_list(self, data):
        '''
        get the mtr list from dict and fill up the list
        '''    
        
        self.list_monte_mtr.clear()
        self.displayed_solver_mtr_list = data    
        
        for key in data:
            #update of list
            QListWidgetItem(str(key), self.list_monte_mtr)
            
        self.list_monte_mtr.repaint()
        msg = "{0} materials in the list".format(len(data))
        self.groupBox_monte_2.setTitle(msg)
        
    def make_monte_carlo(self):
        '''
        takes all selected materials from list (B). 
        Takes number of tasks N.
        Generates N new tasks using numpy random
        '''
        output_dir = self.window().output_dir + SEPARATOR + 'master'
        solver_utils.copy_master_files(\
                           self.window().flow_ini,\
                           output_dir, SEPARATOR)
        self.compute_log_normal_dist()
        self.clear_monte_carlo_list()
        
        
    def save_monte_carlo_results(self):    
        '''
        save results from dict distributions_dict if there are any
        '''
        
        if len(self.distributions_dict) == 0:
            msg = "ERROR - nothing to save"           
            self.messenger(msg)
            return
        
        pocet = int(self.edit_monte_tasks.text())
        poc = len(str(pocet+1))
        
            
        for loop_nr in range(pocet):
            workcopy = copy.deepcopy(self.material)
            
            for mat in self.distributions_dict.keys():
                self.monte_logger.log_message(\
                      loop_nr, mat, workcopy[mat]['type_spec'], self.distributions_dict[mat][loop_nr])
                workcopy[mat]['type_spec'] = self.distributions_dict[mat][loop_nr]   
            
            fdir = '{num:0{width}}'.format(num=loop_nr, width=poc+1)
            fname = self.window().output_dir + fdir + SEPARATOR +  self.window().flow_ini.dict_files['Material']
            
            workcopy.save_changes(fname)
            #ffname = self.window().output_dir + fdir + SEPARATOR + fdir + '_ini.ini'
            #self.create_changed_ini(ffname, Material = self.file_dict['Material'])
            #self.create_launcher_scripts(ffname)
            #self.identify_task('basicProblem', self.output_dir + fdir)
            workcopy = {}  
        
        #if self.launcher_check_hydra.isChecked():
        #    batch.create_cluster_batch(self.output_dir)
        
        self.monte_logger.close()
        msg = "{} new tasks has been created".format(pocet)           
        self.messenger(msg)
        
    def clear_monte_carlo_list(self):
        '''clear selected values from the list'''
        selection = [aaa.data(0) for aaa in self.list_monte_mtr.selectedItems()]
        for item in selection:
            self.displayed_solver_mtr_list.remove(item)
        
        self.list_monte_mtr.clear()    
        self.fill_solver_mtr_list(self.displayed_solver_mtr_list)   
        self.list_monte_mtr.repaint()
        
    def compute_log_normal_dist(self):
        '''
        compute log normal distribution for selected materials
        '''
        
        from numpy.random import lognormal
        from numpy import log 
        selection = [str(list_item.text()) for list_item in self.list_monte_mtr.selectedItems()]
        if not self.edit_monte_sigma.text() or not self.edit_monte_tasks.text():
            msg = "ERROR - please set number of computations and sigma first!"           
            self.messenger(msg)
            return
        
        if len(selection) == 0:
            msg = "ERROR - please select some materials first!"           
            self.messenger(msg)
            return
        
        pocet = int(self.edit_monte_tasks.text())
        sigma =  float(self.edit_monte_sigma.text())
        
        for mat in selection:
            hydraulic_cond = float(self.material[mat]['type_spec'])
            val = lognormal(log(hydraulic_cond), sigma, pocet)
            self.distributions_dict[mat] = val
            
        msg = "{} new values has been computed for each selected material".format(pocet)           
        self.messenger(msg)
        msg = "{0} materials in memory".format(len(self.distributions_dict))
        self.groupBox_monte_buttons.setTitle(msg)
        #cant change number of tasks anymore
        self.edit_monte_tasks.setReadOnly(True) 