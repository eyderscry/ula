'''
1- crear una funcion que cree matrices con numeros aleatorios enteros, apartir de fila y columnas dadas
por el usuario.
2- crear una funcion sumar y restar para dos matrices.

'''
#importar librerias
import numpy as np #falta instalar
import random

#funcion para crear matrices numpy.(en prueba)
def Matriz(r,c):
    #matr = np.array([[],[]],dtype='i')
    #for i in range(r):
        #matr[i] = random.randrange(0,5)#prueba 1
        #for n in range(c):
            #matr[n] = random.randrange(0,5)#prueba 1
    pass


#funcion para crear matrices sin libreria.(en prueba)
"""def Matrizp(r,c):
    fila = []
    colum = []
    for i in range(r):
        append.fila(random.randrange(0,5))
        for n in range(c):
            append.colum(random.randrange(0,5))
    return m[]
"""

#entrada de usuario
#en caso que el usuario ingrese un valor no entero se fijara como 2
try:
    r = int(input("ingrese un numero entero para las filas = "))
except ValueError:
    r = 2

try:
    c = int(input("ingrese un numero entero para las columnas = "))
except ValueError:
    c = 2

print(r,c)