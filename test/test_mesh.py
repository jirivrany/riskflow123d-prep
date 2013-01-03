#!/usr/bin/env python
# coding: utf-8


import app.parser.mesh as mesh

'''

outName = '../../data/out.msh'
p.write(outName)
'''

inpt = '/development/python/RF_test_data/test1.msh'
TEST_MESH = mesh.Mesh()
TEST_MESH.read(inpt)
    
def test_number_of_nodes():
    '''test file contains 322 nodes'''
    assert len(TEST_MESH.nodes) == 322

def test_number_of_elements():
    '''test file contains 1444 elements'''
    assert len(TEST_MESH.elements) == 1444    

def test_second_element():
    '''second element : (1, [62, 21, 0], [83, 84])'''    
    assert TEST_MESH.elements[2] == (1, [62, 21, 0], [83, 84])
    assert TEST_MESH.elements[2][1][1] == 21

