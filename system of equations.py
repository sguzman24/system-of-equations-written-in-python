#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31te 18:23:43 2023

@author: seth guzman
"""


import numpy as np

A = np.array([[2, -1, 3], [-1, 3, -1], [4, -4, 3]])
b = np.array([10, -1, 3])

print("A:\n", A)
print("b:", b)

Ainv = np.linalg.inv(A)

print("\nA inverse:\n", Ainv)

x = Ainv @ b
print("\nx:", x)
