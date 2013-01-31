#!/usr/bin/env python
# coding: utf-8


import app.parser.mesh as mesh
import app.mesh_utils as mesh_utils

'''

outName = '../../data/out.msh'
p.write(outName)
'''

inpt = '/home/albert/riskflow_test_data/rf2_test/mm.msh'
TEST_MESH = mesh.Mesh()
TEST_MESH.read(inpt)
    

def test_import_all_insteps():
    '''
    podezdrele elementy>  16824, 31786 
    a uzly: 3097, 6612
    '''    
    nad = mesh_utils.import_axis(50, TEST_MESH, -1, 'z')
    pod = mesh_utils.import_axis(50, TEST_MESH, 1, 'z')
    skrz = mesh_utils.find_through(50, TEST_MESH, 'z')
    celkem = len(nad) + len(pod) + len(skrz)
    assert 37068 == celkem 
