# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 17:55:19 2023

@author: dania
"""

from matplotlib import pyplot

# Ejemplo: Función lineal.
def f2(x):
    return 4*x + 1
# Valores del eje X que toma el gráfico.
x = range(-10, 15)
# Graficar 

pyplot.plot(x, [f2(i) for i in x])

# Agregando cheturas 
# Establecer el color de los ejes.

pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")

# Limitar los valores de los ejes.
pyplot.xlim(-10, 10)
pyplot.ylim(-10, 10)

# Guardar gráfico como imágen PNG.
pyplot.savefig("output.png")
# Mostrarlo.

pyplot.show()