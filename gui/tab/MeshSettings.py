# -*- coding: utf-8 -*-

'''
@author: Jiri Vrany

Application Settings Tab
'''


from genui.tab.ui_mesh_settings import Ui_MeshSettings
from PyQt4.QtGui import QWidget, QListWidgetItem, QIntValidator


#constants
AXIS_TRANS = {'x':0, 'y':1, 'z':2}

class MeshSettingsTab(QWidget, Ui_MeshSettings):
    '''
    Tab widget for Mesh Settings
    '''
    def __init__(self, parent = None):
        super(MeshSettingsTab, self).__init__(parent)
        self.setupUi(self)
        
        self.displayed_mesh_list = {}
        self.mtr_index_disp_lst = {}
        
        #aliases for objects in main window
        self.messenger = self.window().statusBar.showMessage
        self.msh = self.window().mesh
        
        self.__setup_mesh_control()
        self.fill_mesh_mtr_form()
        
        
    def __setup_mesh_control(self):
        '''
        setup for mesh control block
        '''
        #mesh control
        #self.button_mesh_imp_surface.clicked.connect(self._mesh_import_surface)
        #self.button_mesh_imp_nonzero.clicked.connect(self._mesh_import_nonzero)
        #self.button_mesh_remove_zero.clicked.connect(self._mesh_remove_zero)
        self.button_mesh_import_all.clicked.connect(self._mesh_import_all)
        self.button_mesh_remove_all.clicked.connect(self._mesh_remove_all)
        self.button_mesh_import_mtr.clicked.connect(self._mesh_import_mtr)
        self.button_mesh_remove_mtr.clicked.connect(self._mesh_remove_mtr)
        self.button_mesh_imp_over.clicked.connect(self._mesh_import_over)
        self.button_mesh_imp_bellow.clicked.connect(self._mesh_import_bellow)
        self.button_mesh_rem_over.clicked.connect(self._mesh_remove_over)
        self.button_mesh_rem_bellow.clicked.connect(self._mesh_remove_bellow)
        self.button_mesh_imp_through.clicked.connect(self._mesh_import_through)
        self.button_mesh_rem_through.clicked.connect(self._mesh_remove_through)
        self.button_mesh_imp_elmid.clicked.connect(self._mesh_import_id)
        self.button_mesh_rem_elmid.clicked.connect(self._mesh_remove_id)
        
        self.mesh_list.itemDoubleClicked.connect(self.mesh_go_edit_material)
        self.mesh_list.itemClicked.connect(self._mesh_element_explorer_control)
        self.mesh_radio_z.setChecked(True)
        
        integer_validator = QIntValidator()
        self.mesh_element_id_edit.setValidator(integer_validator)
        self.edit_mesh_crd.setValidator(integer_validator)
      
    def fill_mesh_mtr_form(self):
        '''
        fill form in the mesh editor
        uses app mesh object held by window
        '''
        self.select_mesh_mtr.clear()
        wherefrom = self.window().mesh.mtr_index.keys()
        data = ["%s" % str(k) for k in sorted(wherefrom)]
        self.select_mesh_mtr.insertItems(0, data)
        self.select_mesh_mtr.repaint()
        
    def _mesh_import_list_updater(self, vals=None, todisp=0):
        '''helper for various list update functions
        @PARAM vals {mesh elements}
        @PARAM todisp number of elements for message
        '''
        if vals is not None and len(vals) > 0 : 
            self.displayed_mesh_list.update(vals)
            todisp = len(vals)
            msg = 'Loading %s elements to the list. It may take a while...' % str(todisp)
            self.messenger(msg)
            self.mesh_list_refresh()
            self.messenger('Selection of elements loaded', 8000)
            
    def mesh_list_refresh(self):
        '''
        takes actual dict self.displayedList and refresh the view
        displays - element id, element type, material
        
        creates and refreshes dict of mtr {mtrid : [el1, el2]} 
        '''
        try:
            self.mesh_list.clear()
            self.mtr_index_disp_lst = {}
            
            for key in sorted(self.displayed_mesh_list.keys()):
                #update of list
                mtr = self.displayed_mesh_list[key][1][0]
                tst = "%s %s %s" % (key, self.displayed_mesh_list[key][0], mtr) 
                QListWidgetItem(str(tst), self.mesh_list)
                #update of index
                if self.mtr_index_disp_lst.has_key(mtr):
                    self.mtr_index_disp_lst[mtr].append(key)
                else:
                    self.mtr_index_disp_lst[mtr] = [key]    
           
            #update the default index
            self.msh.mtr_index.update(self.mtr_index_disp_lst)                     
            self.mesh_list.repaint()
            msg = "{0} elements in the list".format(len(self.displayed_mesh_list))
            self.groupBox_2.setTitle(msg)
            
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise            
            
            
    def _mesh_import_all(self):
        '''imports all mesh to list - msh file need to be loaded first'''
        
            
        try:
            msg = 'Loading %s elements to the list. It may take a while...' % str(len(self.msh.elements))
            self.messenger(msg) 
        except AttributeError:
            self.messenger('Error: load MSH data first!', 8000)
        else:
            self.displayed_mesh_list = self.msh.elements.copy()
            self.mesh_list_refresh()
            self.messenger('MSH data loaded', 8000)    
            
    def _mesh_remove_all(self):
        '''
        Clear mesh selected list completely 
        '''
        try:
            self.displayed_mesh_list = {}
            self.mesh_list.clear()
        finally:
            self.messenger('Data removed from list', 8000)
            self.groupBox_2.setTitle('0 elements in the list')
            
    def _mesh_import_mtr(self):
        '''
        import all nodes with material selected in the selec_mtr_mesh
        '''
        idx = int(self.select_mesh_mtr.currentText())
        vals = {}
        for i in self.msh.mtr_index[idx]:
            vals[i] = self.msh.elements[i] 
    
        self._mesh_import_list_updater(vals)
            
    def _mesh_remove_mtr(self):
        '''
        delete all nodes with material selected in the selec_mtr_mesh
        '''
        idx = int(self.select_mesh_mtr.currentText())
        for i in self.msh.mtr_index[idx]:
            del self.displayed_mesh_list[i] 
        
        msg = 'Deleting %s elements from the list. It may take a while...' % str(len(self.msh.mtr_index[idx]))
        self.messenger(msg)
        self.mesh_list_refresh()
        self.messenger('Selection of elements loaded', 8000)
        
    def _mesh_import_list_deleter(self, vals):
        '''
        deletes given values from displayed mesh list
        @param vals: {} of values to be deleted 
        '''
        for key in vals.keys():
            try:
                del(self.displayed_mesh_list[key])
            except KeyError:
                pass
                  
        msg = 'Refreshing the list'
        self.messenger(msg)
        self.mesh_list_refresh()
        self.messenger('Refreshing finished', 8000)
        
    def _get_mesh_axis(self):
        '''
        check what radio is checked, return axis
        @return: axis string identifier
        '''
        if self.mesh_radio_x.isChecked():
            return 'x'
        elif self.mesh_radio_y.isChecked():
            return 'y'
        elif self.mesh_radio_z.isChecked():
            return 'z'
        else:
            self.messenger('Choose axis first!', 8000)
            return False             
        
    def _mesh_import_surface(self):    
        '''
        imports surface elements to mesh list
        need surface_result file to work
        '''
        
        if not self.surface_elements:
            fname = self.work_dir + '/' + 'master/' + FNAME_SURF
            self.surface_elements = surface.read_result(fname) 
                
        vals = {}
        for elid in self.surface_elements:
            elid = int(elid)
            if self.msh.elements.has_key(elid):
                vals[elid] = self.msh.elements[elid]
            
        self._mesh_import_list_updater(vals)
        
    def _mesh_remove_zero(self):
        '''
        removes elemtns with no (zero values) concentration in time from mesh list
        '''
        if not self.result_elements:
            self.read_concentrations()
        
        for key in self.displayed_mesh_list.keys():
            if str(key) not in self.result_elements:
                del(self.displayed_mesh_list[key])
        
        msg = 'Refreshing the list'
        self.messenger(msg)
        self.mesh_list_refresh()
        self.messenger('Refreshing finished', 8000)                     
    
    def _mesh_import_nonzero(self):
        '''
        imports elements with nonzero concentration in time to mesh list
        '''
        if not self.result_elements:
            self.read_concentrations()
            
        vals = {}
        for elid in self.result_elements:
            elid = int(elid)
            if self.msh.elements.has_key(elid):
                vals[elid] = self.msh.elements[elid]
            
        self._mesh_import_list_updater(vals)       
        
        
    def _mesh_import_axis(self, compare, axis = 'z'):
        '''import elements with coordinate in given axis, 
           compare given val with the value of mesh spinbox
        @param compare: -1 for elements bellow, 0 for through, 1 for over 
        @param axix: what axis (x, y, z)
        '''
        val = int(self.edit_mesh_crd.text())
        vals = {}
        for elid, elem in self.msh.elements.items():
            pridat = True
            for node_id in elem[2]:
                node_coord = self.msh.nodes[node_id][AXIS_TRANS[axis]]
                if cmp(node_coord, val) == compare or cmp(node_coord, val) == 0 :
                    pridat = False
            if pridat:
                vals[elid] = self.msh.elements[elid]
        
        return vals
        
    def _mesh_find_through(self, axis = 'z'):
        '''import elements with at last one node over coordinate in given axis,
           such elements has to be cuted through given plane
           compare given val with the value of mesh spinbox
        @param axix: what axis (x, y, z)
        '''
        val = int(self.edit_mesh_crd.text())
        
        vals = {}
        for elid, elem in self.msh.elements.items():
            nad = False
            pod = False
            for node_id in elem[2]:
                node_coord = self.msh.nodes[node_id][AXIS_TRANS[axis]]
                if cmp(node_coord, val) == 1 or cmp(node_coord, val) == 0 :
                    nad = True
                elif cmp(node_coord, val) == -1 or cmp(node_coord, val) == 0 :
                    pod = True
            if nad and pod:
                vals[elid] = self.msh.elements[elid]
        return vals        
    
    def _mesh_import_through(self):
        '''import elements where one node has Z over value of mesh spinbox
        and therefore this element is cut by given alt
        '''
        axis = self._get_mesh_axis()
        if axis:
            vals = self._mesh_find_through(axis)
            self._mesh_import_list_updater(vals)
        
    def _mesh_import_over(self):
        '''import elements where all nodes has Z over value of mesh spinbox
        '''
        axis = self._get_mesh_axis()
        if axis:
            vals = self._mesh_import_axis(-1, axis)
            self._mesh_import_list_updater(vals)
        
    def _mesh_import_bellow(self):
        '''import elements where all nodes has Z bellow value of mesh spinbox
        '''
        axis = self._get_mesh_axis()
        if axis:
            vals = self._mesh_import_axis(1, axis)
            self._mesh_import_list_updater(vals)
            
    def _mesh_import_id(self):
        '''
        Import elemet with id given in form 
        and update displayed list
        '''
        try:
            elmid = int(self.mesh_element_id_edit.text())
            vals = {elmid : self.msh.elements[elmid]}
            self._mesh_import_list_updater(vals)
        except KeyError:
            self.messenger('ERROR: no such element', 8000)
        except ValueError:
            self.messenger('ERROR: not valid element id', 8000)       
    
    def _mesh_remove_id(self):
        '''
        Remove elemet with id given in form  
        and update displayed list
        '''
        elmid = int(self.mesh_element_id_edit.text())
        try:
            vals = {elmid : self.msh.elements[elmid]}
            self._mesh_import_list_deleter(vals)
        except KeyError:
            self.messenger('ERROR: no such element', 8000)                
        
    def _mesh_remove_over(self):
        '''removes elements where all nodes has coordinate in axis
         over value of mesh spinbox
        '''
        axis = self._get_mesh_axis()
        if axis:
            vals = self._mesh_import_axis(-1, axis)
            self._mesh_import_list_deleter(vals)               
        
    def _mesh_remove_bellow(self):
        '''
        removes elements with coordinate in given axis
        bellow value of mesh spinbox
        '''
        axis = self._get_mesh_axis()
        if axis:
            vals = self._mesh_import_axis(1, axis)
            self._mesh_import_list_deleter(vals)
        
    def _mesh_remove_through(self):
        '''
        removes elements cuted through by given plane
        '''
        
        axis = self._get_mesh_axis()
        if axis:
            vals = self._mesh_find_through(axis)
            self._mesh_import_list_deleter(vals)
            
    def _mesh_element_explorer_control(self):
        '''
        action for controling mesh_element_explorer display block
        '''
        idxtu = str(self.mesh_list.currentIndex().data().toString())
        
        idx = idxtu[:idxtu.find(' ')]
        
        doc = "element id: {0}\n".format(idx)
        doc += "node : [x, y, z]\n"
        for node in self.msh.elements[int(idx)][2]:
            doc +=  "{0} : {1}\n".format(node, self.msh.nodes[node])
        self.mesh_element_explorer.clear()
        self.mesh_element_explorer.insertPlainText(doc)
        self.mesh_element_explorer.setReadOnly(True)    
                
    def mesh_go_edit_material(self): 
        '''
        action for double click on displayed mesh list
        '''   
        idxtu = str(self.mesh_list.currentIndex().data().toString())
        _11, _12, mtr = idxtu.split()
        
        idx = self.window().centralWidget.tab_material.selector_material.findText(mtr)
        self.window().centralWidget.tab_material.selector_material.setCurrentIndex(idx)
        self.window().centralWidget.tab_material.get_material_from_dict(mtr)
        self.window().centralWidget.setCurrentIndex(2)