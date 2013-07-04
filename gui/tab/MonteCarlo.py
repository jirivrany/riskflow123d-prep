# -*- coding: utf-8 -*-

'''
@author: Jiri Vrany

RiskFlow 123D
Tab widget for Mesh Tools
'''

from genui.tab.ui_montecarlo import Ui_MonteCarlo
from PyQt4.QtGui import QWidget, QListWidgetItem, QAbstractItemView, QIntValidator

from gui.MyDoubleValidator import MyDoubleValidator
from gui.MyZeroOneValidator import MyZeroOneValidator
from app.helpers import solver_utils
from app.helpers.constants import SEPARATOR
from app.helpers import batch
from app.helpers import monte_carlo

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
        self.__set_validators()
        
        self.monte_logger = monte_logger
        
        #dict of distributions for monte carlo method
        self.computed_conductivity_values = {} 
        self.computed_storativity_values = {}
        self.computed_porosity_values = {}
        
        
        #shortening aliases
        self.messenger = self.window().statusBar.showMessage
        self.material = self.window().material_dict
        
        #fill solver list with materials
        data = sorted(self.material.keys())
        self.fill_solver_mtr_list(data)
        
    
    def __set_validators(self):
        '''
        set validators for edit fields
        '''    
        
        validator_positive_double = MyDoubleValidator(parent = self)
        validator_zero_one = MyZeroOneValidator(self)
        
        
        self.edit_monte_sigma.setValidator(validator_positive_double)
        self.edit_monte_porosity.setValidator(validator_zero_one)
        self.edit_monte_storativity.setValidator(validator_zero_one)
        
        self.edit_monte_tasks.setValidator(QIntValidator())
    
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
        self.window().create_master_task()
        self.compute_log_normal_dist()
        self.clear_monte_carlo_list()
        
        
    def save_monte_carlo_results(self):    
        '''
        save results from dict computed_conductivity_values if there are any
        '''
        
        if len(self.computed_conductivity_values) == 0:
            msg = "ERROR - nothing to save"           
            self.messenger(msg)
            return
        
        pocet = int(self.edit_monte_tasks.text())
        poc = len(str(pocet+1))
        
        local_launcher, cluster_launcher = self.window().get_launchers()
           
        for loop_nr in range(pocet):
            workcopy = copy.deepcopy(self.material)
            
            for mat in self.computed_conductivity_values.keys():
            
                workcopy[mat]['type_spec'] = []
                for direction_value in self.computed_conductivity_values[mat]:
                    
                    self.monte_logger.log_message(\
                          loop_nr, mat, workcopy[mat]['type_spec'], direction_value[loop_nr])
                    workcopy[mat]['type_spec'].append(direction_value[loop_nr])   
                
            
            for mat in self.computed_storativity_values.keys():
                self.monte_logger.log_message(\
                      loop_nr, mat, workcopy[mat]['storativity'], self.computed_storativity_values[mat][loop_nr])
                workcopy[mat]['storativity'] = self.computed_storativity_values[mat][loop_nr]   
            
            for mat in self.computed_porosity_values.keys():
                self.monte_logger.log_message(\
                      loop_nr, mat, workcopy[mat]['dualporosity'], self.computed_porosity_values[mat][loop_nr])
                workcopy[mat]['dualporosity'] = self.computed_porosity_values[mat][loop_nr]      
            
            fdir = '{num:0{width}}'.format(num=loop_nr, width=poc+1)
            fname = self.window().output_dir + fdir + SEPARATOR +  self.window().flow_ini.dict_files['Material']
            
            workcopy.save_changes(fname)
            ffname = self.window().output_dir + fdir + SEPARATOR + fdir + '_ini.ini'
            self.window().flow_ini.create_changed_copy(ffname, Material = self.window().flow_ini.dict_files['Material'])
            
            batch.create_launcher_scripts(ffname, local_launcher, cluster_launcher)
            
            solver_utils.create_task_identifier('basic', self.window().output_dir + fdir)
            workcopy = {}  
        
        if self.window().centralWidget.tab_settings.launcher_check_hydra.isChecked():
            batch.create_cluster_batch(self.window().output_dir)
        
        #self.monte_logger.close()
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
        
        selection = [str(list_item.text()) for list_item in self.list_monte_mtr.selectedItems()]
        
        
        if len(selection) == 0:
            msg = "ERROR - please select some materials first!"           
            self.messenger(msg)
            return
        
        user_set = self.get_sigma_values()
        
        if user_set:
            pocet, sigma, storat, poros = user_set
        else:
            return    
        
        for mat in selection:
            conductivity = self.material[mat]['type_spec']
            val = monte_carlo.compute_conductivity(conductivity, sigma, pocet)
            self.computed_conductivity_values[mat] = val
            
            if storat:
                storativity = self.material[mat]['storativity']
                val = monte_carlo.compute_storativity(storativity, storat, pocet)
                self.computed_storativity_values[mat] = val
                
            if poros:
                porosity = float(self.material[mat]['dualporosity'])
                val = monte_carlo.compute_porosity(porosity, poros, pocet)
                self.computed_porosity_values[mat] = val    
            
        self.message_after_computation(pocet)
        
   
            
        
    def message_after_computation(self, pocet):
        '''
        set message after computation
        '''
        msg = "{} new values has been computed for each selected material".format(pocet)           
        self.messenger(msg)
        msg = "{0} materials in memory".format(len(self.computed_conductivity_values))
        self.groupBox_monte_buttons.setTitle(msg)
        #cant change number of tasks anymore
        self.edit_monte_tasks.setReadOnly(True)
        
        
    def get_sigma_values(self):
        '''
        get sigma values for conductivity, porosity and storativity
        '''
            
        try:
            pocet = int(self.edit_monte_tasks.text())
            conduct =  float(self.edit_monte_sigma.text())
        except ValueError:
            msg = "ERROR - please set number of computations and sigma for conductivity first!"           
            self.messenger(msg)
            return False
        
        try:
            storat =  float(self.edit_monte_storativity.text())
        except ValueError:
            storat = None
        else:
            storat = solver_utils.round_to_positive_zero(storat)
        
        try:        
            porosity = float(self.edit_monte_porosity.text())
        except ValueError:
            porosity = None
        else:
            porosity = solver_utils.round_to_positive_zero(porosity)        
         
        return pocet, conduct, storat, porosity 
         