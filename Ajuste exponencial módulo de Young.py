# -*- coding: utf-8 -*-
"""
Created on Sun May 21 17:34:53 2023

@author: matia
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression
import scipy.stats as stats


#%%

data = pd.read_csv("C:/Users/matia/OneDrive/Escritorio/maximos_medicion_4_acero.csv")
tiempo = data["t"]
intensidad = data["maximos"]


tiempo = tiempo[1:]
intensidad = intensidad[1:]

plt.figure(figsize=(15,4))    
plt.plot(tiempo, intensidad, label = "Datos")  
plt.legend(fontsize = 13)
plt.grid(linestyle='--')
plt.ylabel(r'$Amplitud$ ', fontsize=15)
plt.xlabel(r'$Tiempo$ ', fontsize=15)

#%%funcion ajuste

def func_0(x, A, B, D):
    return A*np.exp(B*x) + D

#%% initial guess
init_guess = [0.8, -2, 0]
param, param_cov = curve_fit(func_0, tiempo, intensidad, p0=init_guess)


x = np.linspace(min(tiempo), max(tiempo), 1000)

plt.figure(figsize=(15,4))
plt.errorbar(tiempo, intensidad,  c='purple', label = "medicion 4 acero", fmt='o',  ecolor='grey', capsize=2, markersize = 7, elinewidth = 2,)
plt.plot(x, func_0(x, param[0], param[1], param[2],), label = 'Ajuste exp')
plt.legend(fontsize = 13)
plt.grid(linestyle='--')
plt.ylabel(r'$Amplitud$ ', fontsize=15)
plt.xlabel(r'$Tiempo$ ', fontsize=15)
plt.grid(which = 'minor',linestyle=':', linewidth='0.1', color='black' )
plt.plot

plt.figure(figsize=(15,4))
x = np.linspace(min(tiempo), max(tiempo), 1000)

plt.errorbar(tiempo, intensidad-func_0(tiempo, param[0], param[1], param[2]), fmt='o', markersize = 7, label = 'Residuo')
plt.axhline(y = 0, color = 'r', linestyle = '--', label = 'y=0')

plt.ylabel(r'$Amplitud$ [mV]', fontsize=15)
plt.xlabel(r'$Distancia$ [Cm]', fontsize=15)

plt.xticks(np.arange(min(tiempo), max(tiempo), 1000))
plt.minorticks_on()
plt.grid(linestyle='--')
plt.grid(which = 'minor',linestyle=':', linewidth='0.1', color='black' )
plt.legend(fontsize = 13)
plt.show()

dec=param[1]

#%% SÉ QUE LA FREC DE ESTA ES 44,39 O 44.66

k_1 = (1.875/0.26)
k_2 = 4.694
I =  6.62
E = 17
den =  4.25
dec = float(param[1])


w = (((I * E) * k_1**(4)/ den) - dec**(2))**(1/2)

#%% 


















