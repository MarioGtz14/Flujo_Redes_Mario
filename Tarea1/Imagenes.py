# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 12:21:24 2019

@author: maari
"""

from PIL import Image
import matplotlib.pyplot as plt


imagen = Image.open("Mario.jpg")
nuevo= imagen.convert('1')

tamaño=imagen.size
print(tamaño)

P = nuevo.load()
ancho, altura = nuevo.size
borrados = 0
vecinos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for fila in range(altura):
    for columna in range(ancho):
        if P[columna, fila] == 0: # pixel es negro
            contador = 0
            for (df, dc) in vecinos:
                vf = fila + df
                vc = columna + dc
                if vf >= 0 and vc >= 0 and vf < altura and vc < ancho: # si existe el vecino
                    if P[vc, vf] == 0:
                        contador += 1
            if contador < 4: # uno o cero vecinos negros
                P[columna, fila] = 255 # será blanco
                borrados += 1
print(borrados, "pixeles negros eliminados")

plt.imshow(nuevo)