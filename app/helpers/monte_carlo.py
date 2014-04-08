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
    
def compute_single_property(method, coeficient, sigma, pocet):
    '''
    computes new property value - for storativty, porosity or geometry_spec
    using log normal distribution
    '''
    met_dic = {
               'storativity': solver_utils.round_storativity,
               'porosity': solver_utils.round_porosity,
               'geometry_spec' : solver_utils.round_to_positive_zero,
               }
    f_coeficient = float(coeficient)
    values = lognormal(log(f_coeficient), sigma, pocet)
    result = []
    for val in values:
        result.append(met_dic[method](val))
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
