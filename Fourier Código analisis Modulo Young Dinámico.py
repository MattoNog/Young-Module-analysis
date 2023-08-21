# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 08:59:59 2023

@author: matia
"""
#%%
import sys
sys.path.append('C:/Users/matia/OneDrive/Escritorio/Labo 4/Young dinámico/fft_funcion_v01.py')
import fft_funcion_v01 as ft

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#%%

path = "C:/Users/matia/OneDrive/Escritorio/Labo 4/Young dinámico/Mediciones/medicion_oscilacion_0.csv" #COMPLETAR CON PATH DE UNO DE LOS ARCHIVOS DE LA CARPETA
formato_data = ".csv" #COMPLETAR
cantidad_mediciones = 8 #COMPLETAR

#%% 

n = 0
path_ppal = path.rstrip('0.csv')
n_archivo = str(n)
formato = str(formato_data)
path_abs = path_ppal + n_archivo + formato


datos = pd.read_csv(path_abs) 

tiempo = datos["tiempo"]
intensidad = datos["intensidad"]

plt.figure(figsize=(15,4))    
plt.title("Medidas Levantadas número " + n_archivo)
plt.plot(tiempo, intensidad, label = "Datos")   
plt.ylabel(r'Amplitud [V]', fontsize=15) 
plt.xlabel(r'Tiempo [s]', fontsize=15)
plt.grid()
plt.plot()

tstep = max(tiempo)/len(tiempo) #0.0005
fsamp = 1/tstep #2000
 
intensidad = np.array(intensidad)

MakeSpectralPlot(intensidad, fsamp)

#%%

for n in range(0,cantidad_mediciones):
    n_archivo = str(n)
    path_ppal = path.rstrip('0.csv')
    path_abs = path_ppal + n_archivo + formato
    guardado_nombre_plot = "Gráfico de medidas " + n_archivo

    datos = pd.read_csv(path_abs) 
    print(path_abs)

    tiempo = datos["tiempo"]
    intensidad = datos["intensidad"]
    
    plt.figure(figsize=(15,4))    
    plt.title("Medidas Levantadas número " + n_archivo)
    plt.plot(tiempo, intensidad, label = "Datos")   
    plt.ylabel(r'Amplitud [V]', fontsize=15) 
    plt.xlabel(r'Tiempo [s]', fontsize=15)
    plt.grid()
    plt.plot()
    plt.savefig(guardado_nombre_plot)
    
    path_ppal = path.rstrip('0.csv')
    n_archivo = str(n)
    formato = str(formato_data)
    path_abs = path_ppal + n_archivo + formato


    datos = pd.read_csv(path_abs) 

    tiempo = datos["tiempo"]
    intensidad = datos["intensidad"]

    tstep = max(tiempo)/len(tiempo) #0.0005
    fsamp = 1/tstep #2000
     
    intensidad = np.array(intensidad)

    MakeSpectralPlot(intensidad, fsamp)
    
