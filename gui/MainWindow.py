# -*- coding: utf-8 -*-
'''
@author: Jiri Vrany

MainWindow of the app. 
Class
'''

from PyQt4.QtGui import QMainWindow, QFileDialog


from gui.MainTabWidget import MainTabWidget
from gui.MainMenu import MainMenu
from gui.MainStatusBar import MainStatusBar
import gui.toolbar
import gui.dialogs

from app.FlowIni import FlowIni

from app.helpers import constants as const
from app.helpers import batch 
 
import app.helpers.output_dir
import app.helpers.solver_utils

import app.parser.material as material
import app.parser.mesh

import app.basic_problem

from os import path


class MainWindow(QMainWindow):
    '''
    Main Application Window
    Factory for main widgets - action bar and tool bar, central tab
    Glue all Widgets together
    '''
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(800, 600)
        
        self.setWindowTitle('RiskFlow')
        
        #central widget is tab
        self.centralWidget = MainTabWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setHidden(True)
        
        self.test_quickstart = False
        
        #main menu of window
        self.menuBar = MainMenu(self)
        self.setMenuBar(self.menuBar)
        self.set_menubar_actions()
        self.menuBar.disable_solver_actions()
        
        #status bar
        self.statusBar = MainStatusBar(self)
        self.setStatusBar(self.statusBar)
        
        self.toolBar = gui.toolbar.MainToolBar(self)
        self.addToolBar(self.toolBar)
        self.action_exit = gui.toolbar.ExitAction()
        self.action_solve = gui.toolbar.SolveAction()
        self.action_quick_start = gui.toolbar.QuickStartAction()
        self.action_solve_2 = gui.toolbar.SolveActionSens()
        
        self.set_toolbar_actions()
        
        #app object
        self.flow_ini = None
        self.material_dict = None
        self.current_problem = None
        self.output_dir = None
        self.mesh = None
        self.setup = None
        
    def set_toolbar_actions(self):
        '''
        set the main common actions for toolbar
        '''
        self.toolBar.addAction(self.action_exit)
        self.toolBar.addAction(self.action_quick_start)
        self.action_exit.triggered.connect(self.on_app_exit)
        self.action_quick_start.triggered.connect(self.quick_start)
        
        
    def set_toolbar_solve_actions(self):
        '''
        set solver actions in toolbar
        '''
        self.toolBar.addAction(self.action_solve)
        self.toolBar.addAction(self.action_solve_2)
            
        self.action_solve.triggered.connect(self.on_action_solve)
        
            
    def set_menubar_actions(self):
        '''
        set actions for menubar
        '''
        self.menuBar.actionOpen.triggered.connect(self.on_ini_file_open)
        self.menuBar.actionExit.triggered.connect(self.on_app_exit)
        self.menuBar.actionSave.triggered.connect(self.on_ini_file_save)
        self.menuBar.actionClose.triggered.connect(self.on_ini_file_close)
        self.menuBar.actionQuick_start.triggered.connect(self.quick_start)    
        
        self.menuBar.actionMonte_Carlo.triggered.connect( \
                             self.on_action_monte_carlo )
        self.menuBar.actionBasic_Problem.triggered.connect(\
                             self.on_action_basic_problem)
        self.menuBar.actionSensitivy_task.triggered.connect( \
                             self.on_action_sensitivity)
        
        
    
    def quick_start(self):
        '''
        quick start last edited ini file
        '''
        file_name = self.centralWidget.tab_settings.setup.values['Work']['Last']    
        self.test_quickstart = True
        self.start_main_routine(file_name)
        
    def on_ini_file_open(self):
        '''
        Action onOpen handler 
        opens file using QFileDialog
        '''
        file_name = QFileDialog.getOpenFileName(self, \
                        "Open File", ".", \
                        "Flow ini (*.ini)\nAll Files (*.*)")
        
        if file_name:
            self.on_ini_file_close()
            self.start_main_routine(str(file_name))
        
    def on_ini_file_close(self):
        '''
        when ini file is closed application has to close all related stuff
        '''
        self.flow_ini = None
        self.material_dict = None
        self.current_problem = None
        self.output_dir = None
        self.mesh = None
        
        self.centralWidget.remove_solver_tabs()
        self.centralWidget.hide()
        
    def start_main_routine(self, fname):
        '''
        Call handler in tab_flow_ini Widget
        Calls Factory methods for Material and Mesh objects
        Display result message 
        '''
             
        try:
            self.flow_ini = FlowIni(fname)
        except TypeError:
            self.statusBar.showMessage("Error reading flow ini file") 
        else:        
            if self.centralWidget.tab_flow_ini.handle_file(self.flow_ini):
                self.try_enable_solver_actions()
            else:
                self.menuBar.disable_solver_actions()
                self.statusBar.showMessage('ERROR in ini file', 8000)
                
            self.setup = self.centralWidget.tab_settings.setup.values
            #Enable central widget
            self.centralWidget.setHidden(False)
            #enable flow ini edtior
            self.centralWidget.tab_flow_ini.set_writable()
            
       
                
    def try_enable_solver_actions(self):
        '''
        enable or disable solver actions according to the settings
        '''
        if hasattr(self.centralWidget, 'tab_settings'):
            if self.centralWidget.tab_settings.check_launchers():
                self.menuBar.enable_solver_actions()
            else:
                self.menuBar.disable_solver_actions()
                self.statusBar.showMessage('ERROR : Check at last one type of launcher in settings please.')
                
    def on_ini_file_save(self):
        '''
        Action onSave handler
        save changes from editor
        '''
        fname = self.flow_ini.file_name
        if self.centralWidget.tab_flow_ini.dialog_ini_file_save(fname):
            self.start_main_routine(fname)
            
                
    def load_material(self):
        '''
        Executed after sucessfull check of flow.ini file
        Factory for MaterialDict - prepares object for application
        '''
        try:
            self.material_dict = material.MaterialDict(self.flow_ini.get_material_file_name())
        except material.EmptyListException:
            self.statusBar.showMessage('Error loading material from file', 8000)
        finally:
            self.statusBar.showMessage('Material file loaded', 8000)
    
    def load_mesh(self):
        '''
        Executed after sucessfull check of flow.ini file
        Factory for Mesh - prepares object for application
        load mesh using mesh module
        '''            
        file_name = self.flow_ini.get_mesh_file_name()
        self.statusBar.showMessage('Loading mesh file. It may take a while') 
        self.mesh = app.parser.mesh.Mesh()
        self.mesh.read(file_name)
        self.statusBar.showMessage('Mesh file loaded successfully') 
    
                
    def on_app_exit(self):
        '''
        When user exit the app by button
        Save last used ini file for quick start next time
        '''
        setup = self.centralWidget.tab_settings.setup
        try:
            setup.values['Work']['Last'] = self.flow_ini.file_name
        except AttributeError:
            pass    
        setup.save_settings()
        self.close()
        
    def on_action_basic_problem(self):
        '''
        slot for action basic problem signal
        prepares all necesities for basic solver problem
        '''
        problem_type = 'basic'
        if self.set_output_dir(problem_type):
            self.common_solver_setup(problem_type)
            self.centralWidget.add_basic_problem_tabs()
            
            self.set_toolbar_solve_actions()
            self.action_solve.setText('Generate Task')
            self.toolBar.removeAction(self.action_solve_2)
        else:
            self.backup_warning()        
        
    def on_action_monte_carlo(self):
        '''
        slot for action monte carlo signal
        prepares all necesities for monte carlo problem
        '''
        problem_type = 'monte'
        if self.set_output_dir(problem_type):
            self.common_solver_setup(problem_type)
            self.centralWidget.add_monte_carlo_tabs()
            
            self.set_toolbar_solve_actions()
            self.action_solve.setText('Generate Tasks')
            self.toolBar.removeAction(self.action_solve_2)
        else:
            self.backup_warning()    
        
    def on_action_sensitivity(self):
        '''
        slot for action sensitivity problem signal
        prepares all necesities for sensitivity solver problem
        '''
        problem_type = 'sens'
        append = self.set_output_dir(problem_type)
        if append:
            self.common_solver_setup(problem_type)
            self.centralWidget.add_sensitivity_task_tabs()
            self.centralWidget.tab_sensitivity.set_initial_count(append)
            
            self.set_toolbar_solve_actions()
            self.action_solve.setText('Multiplier x Material')
            self.action_solve_2.triggered.connect(self.centralWidget.tab_sensitivity.make_sens_multiplication_group)       
        
        else:
            self.backup_warning()        
            
    def backup_warning(self):
        '''
        display a message with backup warning
        '''
        result = "Make backup of you previous work, and try again."
        self.statusBar.showMessage(result)
                
        
    def set_output_dir(self, problem_type):    
        '''
        sets empty output dir
        '''
        output_dir = app.helpers.output_dir.set_output_dir(\
                               self.flow_ini.dir_name, problem_type)
        
        
        if app.helpers.output_dir.exist(output_dir):
            if app.helpers.output_dir.is_not_empty(output_dir):
                if problem_type == 'sens':
                    return self.output_dir_sens(output_dir)
                else:
                    return self.output_dir_monte_basic(output_dir)      
            else:
                result = "Output dir exists and is empty"
                
        else:        
            result = app.helpers.output_dir.create(output_dir)
        
        self.output_dir = output_dir
        
        self.statusBar.showMessage(result, 8000, self.output_dir)
        return True
    
    def output_dir_sens(self, output_dir):
        '''
        outputdir dialog and delete for sensitivity
        '''
        return_code = gui.dialogs.append_or_empty_output_dir(self, output_dir)
        if return_code == 0:
            self.delete_output_dir(output_dir)
            self.output_dir = output_dir
            return True
        elif return_code == 2:
            count = app.helpers.output_dir.get_max_dir_number(output_dir)
            self.output_dir = output_dir
            return count
        else:
            return False         
        
        
    def output_dir_monte_basic(self, output_dir):
        '''
        deletes the data for monte and basic after confirm
        '''
        delete_it = gui.dialogs.empty_output_dir(self, output_dir)
        if delete_it:
            self.delete_output_dir(output_dir)
            self.output_dir = output_dir
            return True
        else:
            return False  
    
    def delete_output_dir(self, output_dir):
        '''
        delete content of output dir
        '''
        app.helpers.output_dir.delete_content(output_dir)
        result = "Obsolete content of {} has been deleted.".format(output_dir)
        self.statusBar.showMessage(result, 8000, self.output_dir)    
        
    def common_solver_setup(self, problem_type):
        '''
        common settings for all solvers, dispatch by problem type
        '''
        #editor read  only from now
        self.centralWidget.tab_flow_ini.set_read_only()
        
        #load material
        if not self.material_dict:
            self.load_material()
        #and mesh
        if not self.mesh:
            self.load_mesh()
        
        app.helpers.solver_utils.create_task_identifier(problem_type, self.output_dir)
        app.helpers.solver_utils.copy_master_files(self.flow_ini, self.output_dir, const.SEPARATOR)
        
        self.current_problem = problem_type
        
    def on_action_solve(self):
        '''
        slot for action solve (run solver)
        dispatching on current problem type
        '''
        possible_methods = {
            'basic' : self.solve_basic_problem,
            'monte' : self.solve_monte_carlo,
            'sens' : self.solve_sensitivity_task,
            }
        try:
            possible_methods[self.current_problem]()
        except KeyError:
            self.statusBar.showMessage("Can't run - first open some problem to solve")
        
    def solve_basic_problem(self):
        '''
        calls method from basic_problem module with correct data
        save all changes to material file
        creates launchers
        '''
        app.basic_problem.save_material(\
                self.output_dir, self.flow_ini.dict_files['Material'], self.material_dict)
        
        local_launcher, cluster_launcher = self.get_launchers()
        ini_name = self.output_dir + const.SEPARATOR + path.split(self.flow_ini.file_name)[1]
        batch.create_launcher_scripts(ini_name, local_launcher, cluster_launcher)
        
        self.statusBar.showMessage('All changes was saved to disk')
        
    def solve_monte_carlo(self):
        '''
        save monte carlo results to disk
        '''
        self.centralWidget.tab_montecarlo.save_monte_carlo_results()
    
    def solve_sensitivity_task(self):
        '''
        @todo: implement this stub
        '''
        self.centralWidget.tab_sensitivity.make_sens_multiplication()
    
    def create_master_task(self):
        '''
        creates master tasks using solver_utils
        '''
        
        output_dir = self.window().output_dir + const.SEPARATOR + 'master'
        local_launcher, cluster_launcher = self.get_launchers()
        
        
        ini_name = output_dir + const.SEPARATOR + path.split(self.flow_ini.file_name)[1]
            
        app.helpers.solver_utils.copy_master_files(\
                           self.flow_ini,\
                           output_dir, const.SEPARATOR)
        
        #save last changes
        app.basic_problem.save_material(\
                output_dir, self.flow_ini.dict_files['Material'], self.material_dict)
        
        batch.create_launcher_scripts(ini_name, local_launcher, cluster_launcher)
        
    
    def get_launchers(self):
        '''
        check app setup for launchers config and names
        '''
        local_launcher = False
        cluster_launcher = False
        if self.setup['Launcher']['Local']:
            local_launcher = self.setup['Launcher']['Local_bin']
            
        if self.setup['Launcher']['Cluster']:
            cluster_launcher = self.setup['Launcher']['Cluster_bin']
            if not cluster_launcher:
                cluster_launcher = True
                
        return local_launcher, cluster_launcher