#!/usr/bin/env python
"""Based on Mesh Class by Carl Osterwisch <osterwischc@asme.org>, January 2005
    Mesh -- A class for storing nodes and elements.

"""

class Mesh(object):
    """This is a class for storing nodes and elements.

    Members:
    nodes -- A dict of the form { nodenode_id: [ xcoord, ycoord, zcoord] }
    elements -- A dict of the form { elemnode_id: (type, [tags], [nodenode_ids]) }
    mtr_index == A dict with index of materials - { element tag nr. 1 : [elmnode_id]}
    elm_index == A dict with index of elements - { nodenode_id : [elmnodeids] }
    
    Methods:
    read(file) -- Parse a Gmsh version 1.0 or 2.0 mesh file
    write(file) -- Output a Gmsh version 2.0 mesh file
    """

    def __init__(self):
        self.read_finished = False
        self.read_tick = 0
        self.nodes = {}
        self.elements = {}
        self.mtr_index = {}
        self.elm_index = {}
        self.line = None

    def read(self, fname):
        """Read a Gmsh .msh file.
        
        Reads Gmsh format 1.0 and 2.0 mesh files, storing the nodes and
        elements in the appropriate dicts.
        """

        readmode = 0
        mshfile = open(fname,"r")
        for line in mshfile:
            self.line = line.strip()
            if self.line.startswith('$'):
                readmode = get_read_mode(self.line)
            elif readmode:
                columns = line.split()
                if readmode == 1 and len(columns) == 4:
                    readmode = self.__read_nodes(columns, readmode)
                    
                elif readmode > 1 and len(columns) > 5:
                    # Version 1.0 or 2.0 Elements 
                    try:
                        columns = [int(val) for val in columns]
                    except ValueError:
                        print 'Element format error: ' + self.line
                        readmode = 0
                    else:
                        self.__read_elements(columns, readmode)
    
    def __read_nodes(self, columns, readmode):
        '''Read version 1.0 or 2.0 Nodes'''
        try:
            self.nodes[int(columns[0])] = [float(val) for val in columns[1:]]
        except ValueError:
            print 'Node format error: ' + self.line
            return 0
        else:
            return readmode
  
    def __read_elements(self, columns, readmode):
        '''
        Read version 1.0 or 2.0 elements
        '''
        (node_id, node_type) = columns[0:2]
        if readmode == 2:
            # Version 1.0 Elements
            tags = columns[2:4]
            nodes = columns[5:]
        else:
            # Version 2.0 Elements
            ntags = columns[2]
            tags = columns[3:3+ntags]
            nodes = columns[3+ntags:]
        self.elements[node_id] = (node_type, tags, nodes)
        
        #create elm index
        for curent_node in nodes:
            if self.elm_index.has_key(curent_node):
                self.elm_index[curent_node].append(node_id)
            else:
                self.elm_index[curent_node] = [node_id,]
        
        #create mtr index
        if self.mtr_index.has_key(tags[0]):
            self.mtr_index[tags[0]].append(node_id)
        else:
            self.mtr_index[tags[0]] = [node_id,]  

    def write(self, fname):
        """
        Dump the mesh out to a Gmsh 2.0 msh file_output.
        """
        file_output = open(fname,"w")
        
        print >> file_output, '$MeshFormat\n2.0 0 8\n$EndMeshFormat'
        print >> file_output, '$Nodes\n%d' % len(self.nodes)
        for (node_id, coord) in self.nodes.items():
            print >> file_output, node_id, ' '.join([str(val) for val in coord])
        print >> file_output, '$EndNodes'
        print >> file_output, '$Elements\n%d' % len(self.elements)
        for (node_id, elem) in self.elements.items():
            (node_type, tags, nodes) = elem
            print >> file_output, node_id, node_type, len(tags),
            print >> file_output, ' '.join([str(val) for val in tags]),
            print >> file_output, ' '.join([str(val) for val in nodes])
        print >> file_output, '$EndElements'


def get_read_mode(line):
    '''
    sets the readmode
    '''
    if line == '$NOD' or line == '$Nodes':
        return 1
    elif line == '$ELM':
        return 2
    elif line == '$Elements':
        return 3
    else:
        return 0
            
