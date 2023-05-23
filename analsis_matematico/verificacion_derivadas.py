# -*- coding: utf-8 -*-
"""
Created on Mon May 22 21:17:35 2023

@author: dania
"""
#ALgunos ejemplos de verificación de derivada con Python

import sympy

#Declaramos los símbolos que usaremos
x, y = sympy.symbols('x y')

#Podemos etiquetar la función primero y luego usar la variable para derivar:
y = x**3-3*x+2
print(sympy.diff(y))

#O podemos derivar la expresión directamente
print(sympy.diff(sympy.sqrt(x)))