# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:14:23 2023

@author: matia
"""

import uncertainties as unc
import uncertainties.unumpy as unp
import numpy as np

#%% Acero

k = 1.875

d = 0.00602
d_err = 0.00001

l = 0.51
l_err = 0.01

m =  331.0512
m_err= 8.1252

M = 0.11998
M_err= 0.002

d = unc.ufloat(d, d_err)  
l = unc.ufloat(l, l_err)
m = unc.ufloat(m, m_err)  
M = unc.ufloat(M, M_err)

def E(M, m, l, d, k):
    resultado = (m * M * 64) / (k**(4) * l * np.pi * d**(4))
    return resultado

result = E(M, m, l, d, k)


print("E:", result / 10**(6), "MPa")
print("E con error:", unp.nominal_values(result) / 10**(6), "+/-", unp.std_devs(result) / 10**(6), "MPa")

#%% Latón

k = 1.875

d = 0.00505
d_err = 0.00001

l = 0.5
l_err = 0.01

m =  95.6600
m_err= 1.40

M = 0.09104
M_err= 0.0002

d = unc.ufloat(d, d_err)  
l = unc.ufloat(l, l_err)
m = unc.ufloat(m, m_err)  
M = unc.ufloat(M, M_err)

def E(M, m, l, d, k):
    resultado = (m * M * 64) / (k**(4) * l * np.pi * d**(4))
    return resultado

result = E(M, m, l, d, k)


print("E:", result / 10**(6), "MPa")
print("E con error:", unp.nominal_values(result) / 10**(6), "+/-", unp.std_devs(result) / 10**(6), "MPa")