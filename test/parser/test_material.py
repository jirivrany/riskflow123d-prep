#!/usr/bin/env python
# coding: utf-8


import app.parser.material as material

import pytest

TEST_KEYS = ['9617', '9207', '4300', '9612', '9200', '9107', '9100', '4100', '9400', '4200', '9307', '9300', '2200', '2207', '9517', '9312', '1112', '9407', '1117', '9512', '9600', '9607', '9500', '9112', '9317', '9507', '9117', '4500', '9212', '9217', '4600', '2212', '2217', '4400', '1107', '9412', '1100', '9417']

MOCK_KEY = '9500'
MOCK_MATERIAL = {
                 'type': '31',
                 'type_spec': ['0.0056306766']
                 }

MOCK_MATERIAL['storativity'] = '0.01'
MOCK_MATERIAL['sorption'] = '0.00'
MOCK_MATERIAL['dualporosity'] = '0.05'
MOCK_MATERIAL['sorptionfraction'] = '0.00'
MOCK_MATERIAL['geometry_type'] = None
MOCK_MATERIAL['geometry_spec'] = None
MOCK_MATERIAL['reactions'] = None

MOCK_COLLECTION = {
                   'materials' : ['9500\t31\t0.0056306766'],
                   'storativity' : ['9500\t0.01',],
                   'sorption' : ['9500\t0.00',],
                   'dualporosity' : ['9500\t0.05'],
                   'sorptionfraction' : ['9500\t0.00',],
                   'geometry' : [],
                   'reactions' : [],
               }


inpt = '/home/albert/riskflow_test_data/rf2_test/material/mm.mtr'
TEST_MAT = material.MaterialDict(inpt)
    
def test_file_load():
    '''it should load the file and compare keys with mock test_keys'''
    assert TEST_KEYS == TEST_MAT.keys()
    
def test_secific_values():
    '''it should test one element from loaded file, it it was created in order'''
    assert TEST_MAT[MOCK_KEY] == MOCK_MATERIAL        

        
def test_create_collections():
    '''it should convert data to list'''
    inpt = '/home/albert/riskflow_test_data/rf2_test/material/mock.mtr'
    mock_mat = material.MaterialDict(inpt)
    assert mock_mat.create_collections() == MOCK_COLLECTION
    
def test_write_changes():
    '''it should make a copy of original file, the copy should have identical number of lines'''
    inpt = '/home/albert/riskflow_test_data/rf2_test/material/mm.mtr'
    tsss = material.MaterialDict(inpt)
    oooo = '/home/albert/riskflow_test_data/rf2_test/material/mm-output.mtr'            
    tsss.save_changes(oooo)
    original = open(inpt).readlines() 
    newfile = open(oooo).readlines()
    
    assert len(original) == len(newfile)
    
def test_multiply_type_spec():
    '''
    type_spec for all elements should be multipled
    type spec is hydraulict conductivity
    '''       
    inpt = '/home/albert/riskflow_test_data/rf2_test/material/mm.mtr'
    my_test_dict = material.MaterialDict(inpt)
    prop_name = 'type_spec'
    multip = 100
    my_test_dict.multiply_property(prop_name, my_test_dict, multip)
    assert my_test_dict['9617'][prop_name] == [0.1816229383 * 100, 3.5 * 100, 2.5 * 100]
    assert my_test_dict['4300'][prop_name] == [1629.9762434558 * 100, ]
    
def test_set_hydraulic_cond():
    '''
    type_spec for all elements should be new constant values
    '''       
    inpt = '/home/albert/riskflow_test_data/rf2_test/material/mm.mtr'
    my_test_dict = material.MaterialDict(inpt)
    prop_name = 'type_spec'
    new_values = ['10','20', '0']
    my_test_dict.set_property_value(prop_name, my_test_dict, new_values)
    assert my_test_dict['4100'][prop_name] == new_values[:2]
    assert my_test_dict['9617'][prop_name] == new_values
    assert my_test_dict['4300'][prop_name] == new_values[:1] 
    
def test_new_value_norm():
    '''
    new values for storativty and porosity must be in <0.0001, 0.9999>
    '''
    inpt = '/home/albert/riskflow_test_data/rf2_test/material/mm.mtr'
    my_test_dict = material.MaterialDict(inpt)
    prop_name = 'storativity'
    new_values = 100
    my_test_dict.set_property_value(prop_name, my_test_dict, new_values)
    assert my_test_dict['4100'][prop_name] == '0.99999'