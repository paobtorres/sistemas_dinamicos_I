# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 21:41:17 2022

@author: dania

Ejercicio 1 taller 4 Límite
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def l(v):
    return np.sqrt(1-v**2/(3E+8)**2)


v = np.array([2.99999997E+8,2.99999998E+8,2.99999999E+8])

#Para crear n cantidad de valores se puede comentar la linea anterior (agregando # al inicio de la inea) y descomentar las siguientes lineas
#start = 1 # Este es el valor donde quieren iniciar la tabla
#stop = 1e8 #Este es el valor final de la tabla 
#n_valores #esta es la cantidad de valores que quieren
#v = np.linspace (start,stop, num=n_valores)

print(l(v))     

tabla = pd.DataFrame( list(zip(v, l(v))), columns=['v', 'l'] )

print(tabla)
