# -*- coding: utf-8 -*-

'''
Created on 4.7.2013

@author: Jiri Vrany
'''
from numpy.random import lognormal
from numpy import log

def compute_conductivity(material_type_spec, sigma, pocet):
    '''
    computes new hydraulic conductivity value, for all directions
    using log normal distribution
    '''
    result = []
    
    for direction_value in material_type_spec:
        hydraulic_cond = float(direction_value)
        val = lognormal(log(hydraulic_cond), sigma, pocet)
        result.append(val)
        
    return result
    
def compute_storativity(storativity, storat, pocet):
    '''
    computes new storativity value
    using log normal distribution
    '''
    storativity = float(storativity)
    val = lognormal(log(storativity), storat, pocet)
    return val

def compute_porosity(porosity, poros, pocet):
    '''
    computes new dual porosity value
    using log normal distribution
    '''
    porosity = float(porosity)
    val = lognormal(log(porosity), poros, pocet)
    return val