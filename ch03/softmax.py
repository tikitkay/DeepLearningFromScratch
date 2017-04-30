# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 14:42:49 2017

@author: pc
"""

import numpy as np


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    
    return y
    

