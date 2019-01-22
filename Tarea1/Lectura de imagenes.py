# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 11:31:27 2019

@author: maari
"""

from skimage import io
import matplotlib.pyplot as plt

imagen=io.imread("Mario.jpg")/255.0

print("- Dimensiones de la imagen:")
print(imagen.shape)
plt.imshow(imagen)

plt.imshow(imagen[:,:,1])
plt.title("Canal Verde")
plt.figure()


'''
plt.imshow(lena_rgb[:,:,1],vmin=0,vmax=1)
plt.title("Canal Verde")
plt.figure()
'''


