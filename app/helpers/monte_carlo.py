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
    
def compute_storativity_porosity(coeficient, sigma, pocet):
    '''
    computes new storativity or porosity value
    using log normal distribution
    '''
    f_coeficient = float(coeficient)
    values = lognormal(log(f_coeficient), sigma, pocet)
    result = []
    for val in values:
        result.append(solver_utils.normalize_result_stora_poro(val))
    
    return result

def compute_sorption(sorption_dict, sorption_values, pocet):
    '''
    computes new sorption values for substances stored in sorption dict
    '''
    result = {}
    for subst_nr, subst_sorption in sorption_dict.iteritems():
        f_subst_sorption = float(subst_sorption)
        sigma = sorption_values[subst_nr]
        values = lognormal(log(f_subst_sorption), sigma, pocet)
        result[subst_nr] = values
        
    return result
