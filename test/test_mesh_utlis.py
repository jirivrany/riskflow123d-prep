#!/usr/bin/env python
# coding: utf-8


import app.parser.mesh as mesh

'''

outName = '../../data/out.msh'
p.write(outName)
'''

inpt = '/home/albert/riskflow_test_data/test1.msh'
TEST_MESH = mesh.Mesh()
TEST_MESH.read(inpt)
    

def test_second_element():
    '''second element : (1, [62, 21, 0], [83, 84])'''    
    print TEST_MESH.elements
    print TEST_MESH.nodes
    assert False
