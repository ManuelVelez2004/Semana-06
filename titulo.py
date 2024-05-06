# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:06:52 2024

@author: Dell
"""

# Importamos la libreria
import camelcase

nombre = "manuel silverio velez de villa huacachi"

print(nombre.upper())
print(nombre.title())


#Creamos un objeto llamado cam
cam = camelcase.CamelCase()
print("Con camelcase....")

# imprimimos el nombre en formato título
# utilizamos camelcase
print(cam.hump(nombre))

# Para resolver el problema
# creamos otro objeto llamado cam2
# al definir el objeto, incluimos los argumentos
# 'flor' y 'león' 
cam2 = camelcase.CamelCase('manuel','huacachi')
print(cam2.hump(nombre))

