# -*- coding: utf-8 -*-
"""
Created on Tue May  2 09:08:00 2017

@author: pc
"""
import numpy as np


def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)
    

def cross_entropy_error(y, t):
    delta = 1e-7  #절대 0이 되서 무한대로 오차가 가지 않도록 아주 작은 값을 더함 
    return -np.sum(t * np.log(y+delta))
    
