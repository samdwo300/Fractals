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
    iterations = 10
    c = complex(a,b)
    z = c
    for i in range(iterations):
        if abs(z**2 + c) > 2 and i <= 1 and i<=2:
            return (0,0,0)
        elif abs(z**2 + c) > 2 and i <= 3 and i<=4:
            return (255,48,48)
        elif abs(z**2 + c) > 2 and i <= 5 and i<=6:
            return (205,16,118)
            break
        elif abs(z**2 + c) > 2 and i <= 7 and i<=8:
            return (139,10,80)
            break
        elif abs(z**2 + c) > 2 and i <= 9 and i<= 10:
            return (30,144,255)
            break     
        z = z**2 + c
    return (0,0,0)

 
    
# creating the new image in RGB mode 
img = Image.new('RGB', (500,500)) 
pixels = img.load() 




for x in range(img.size[0]):  
    for y in range(img.size[1]):
        pixels[x, y] = mandelbrot_sequence((x/(500/4))-2,(y/(500/4))-2)

# Crop image below

width, height = img.size   # Get dimensions
left = width
top = height
right = width/2
bottom = height
cropped = img.crop((left, top, right, bottom))

cropped.show()
# completing the given number of iterations 
img.show() 
img.save("out.jpg", "JPEG", quality=80, optimize=True, progressive=True)
















