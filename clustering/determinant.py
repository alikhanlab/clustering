#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 17:03:10 2019

@author: alikhannurlanuly
"""

def determinant(A):
    
    rows = A.shape[0]
    if rows(A) == 1:
        return A[0][0]
    
    sign = 1
    first_row = A[0]
    det = 0
    
    def strip_row_col(A, i):
        import numpy as np
        return np.delete(A, i, axis = 1)
        
        
        
        
    for i in range(first_row):
        sub_matrix = strip_row_col(A, i)
        det += sign * first_row[i] * determinant(sub_matrix)
        sign *= -1
    
    return det