'''
Created on 31.1.2013

@author: Jiri Vrany
'''
#constants
AXIS_TRANS = {'x':0, 'y':1, 'z':2}

def import_axis(val, mesh, compare, axis = 'z'):
    '''import elements with coordinate in given axis, 
       compare given val with the value of mesh spinbox
    @param compare: -1 for elements bellow, 0 for through, 1 for over 
    @param axis: what axis (x, y, z)
    '''
    vals = {}
    for elid, elem in mesh.elements.items():
        pridat = True
        for node_id in elem[2]:
            node_coord = mesh.nodes[node_id][AXIS_TRANS[axis]]
            if cmp(node_coord, val) == compare or cmp(node_coord, val) == 0 :
                pridat = False
        if pridat:
            vals[elid] = mesh.elements[elid]
    
    return vals

def find_through(val, mesh, axis = 'z'):
    '''
    import elements with at last one node over coordinate in given axis,
       such elements has to be cuted through given plane
       compare given val with the value of mesh spinbox
    @param axis: what axis (x, y, z)
    '''
    
    vals = {}
    for elid, elem in mesh.elements.items():
        nad = False
        pod = False
        for node_id in elem[2]:
            node_coord = mesh.nodes[node_id][AXIS_TRANS[axis]]
            
            #is over or in touch
            if cmp(node_coord, val) == 1 or cmp(node_coord, val) == 0 :
                nad = True
            
            #is bellow or in touch
            if cmp(node_coord, val) == -1 or cmp(node_coord, val) == 0 :
                pod = True
            
                
        if nad and pod:
            vals[elid] = mesh.elements[elid]
            
            
           
    return vals        
