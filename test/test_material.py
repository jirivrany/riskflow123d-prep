#!/usr/bin/env python
# coding: utf-8


import app.parser.material as material

import pytest

TEST_KEYS = ['9617', '9207', '4300', '9612', '9200', '9107', '9100', '4100', '9400', '4200', '9307', '9300', '2200', '2207', '9517', '9312', '1112', '9407', '1117', '9512', '9600', '9607', '9500', '9112', '9317', '9507', '9117', '4500', '9212', '9217', '4600', '2212', '2217', '4400', '1107', '9412', '1100', '9417']

MOCK_KEY = '9500'
MOCK_MATERIAL = {
                 'type': '31',
                 'type_spec': [0.0056306766,]
                 }

MOCK_MATERIAL['storativity'] = [0.01,]
MOCK_MATERIAL['sorption'] = [0.0,]
MOCK_MATERIAL['dualporosity'] = [0.05,]
MOCK_MATERIAL['sorptionfraction'] = [0.0,]
MOCK_MATERIAL['geometry'] = []
MOCK_MATERIAL['reactions'] = []


inpt = '/development/python/rf2/test/data/material/mm.mtr'
TEST_MAT = material.MaterialDict(inpt)
    
def test_file_load():
    '''it should load the file and compare keys with mock test_keys'''
    assert TEST_KEYS == TEST_MAT.keys()
    
def test_secific_values():
    '''it should test one element from loaded file, it it was created in order'''
    assert TEST_MAT[MOCK_KEY] == MOCK_MATERIAL        

def test_bad_load():
    inpt = '/development/python/rf2/test/data/material/mtr_v5_10_2.mtr'
    with pytest.raises(material.EmptyListException):
        p = material.MaterialDict(inpt)
        print p
    
