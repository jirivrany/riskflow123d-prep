# -*- coding: utf-8 -*-

'''
Created on 4.7.2013

@author: Jiri Vrany
'''
from numpy.random import lognormal
from numpy import log
import solver_utils


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
    
def compute_storativity_porosity(coeficient, values, pocet):
    '''
    computes new storativity value
    using log normal distribution
    '''
    f_coeficient = float(coeficient)
    values = lognormal(log(f_coeficient), values, pocet)
    result = []
    for val in values:
        result.append(solver_utils.normalize_result_stora_poro(val))
    
    return result
