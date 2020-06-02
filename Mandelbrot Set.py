# -*- coding: utf-8 -*-
"""
Created on Thu May 14 10:42:13 2020
Attempt to graph the Mandelbrot set
@author: samdw
"""
import numpy as np
import  pandas as pd
import matplotlib as plt
import random as rd
from PIL import Image
import colorsys 
# z_n = Z_n-1 + c
# Z_0 = 0
 



# For a given c this function returns True if c is in the Mandelbrot set for a
#  given iteration threshhold and False otherwise
def mandelbrot_sequence(a,b):
    iterations = 100
    c = complex(a,b)
    z = c
    for i in range(iterations):
        if abs(z**2 + c) > 2 and i<=10:
            return (99,184,255)
        elif abs(z**2 + c) > 2 and i >= 11 and i<=20:
            return (205,16,118)
            break
        elif abs(z**2 + c) > 2 and i >= 21 and i<=30:
            return (139,10,80)
            break
        elif abs(z**2 + c) > 2 and i >= 31 and i<= 40:
            return (30,144,255)
            break  
        elif abs(z**2 + c) > 2  and i >= 41 and i<= 50:
            return (120,22,35)
            break  
        elif abs(z**2 + c) > 2  and i >= 51 and i<= 60:
            return (100,144,255)
            break    
        elif abs(z**2 + c) > 2  and i >= 61 and i<= 70:
            return (30,144,3)
            break    
        elif abs(z**2 + c) > 2  and i >= 71 and i<= 80:
            return (49,40,20)
            break    
        elif abs(z**2 + c) > 2  and i >= 81 and i<= 90:
            return (238,180,34)
            break 
        elif abs(z**2 + c) > 2  and i >= 91 and i<= 100:
            return (50,180,200)
            break    
        z = z**2 + c
    return (255,99,71)

 
    
# creating the new image in RGB mode 
img = Image.new('RGB', (500,500)) 
pixels = img.load() 




for x in range(img.size[0]):  
    for y in range(img.size[1]):
        pixels[x, y] = mandelbrot_sequence((x/(500/4))-2,(y/(500/4))-2)

# Crop image below


left = 0
top = 100
right = 325
bottom = 400
cropped = img.crop((left, top, right, bottom))

cropped.show()
# completing the given number of iterations 

cropped.save("out.jpg", "JPEG", quality=80, optimize=True, progressive=True)
















