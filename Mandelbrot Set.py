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
        if abs(z**2 + c) > 2:
            return (70,130,180)
            break
        z = z**2 + c
    return (84,255,159)

    
# creating the new image in RGB mode 
img = Image.new('RGB', (500,500)) 
pixels = img.load() 




for x in range(img.size[0]):  
    for y in range(img.size[1]):
        pixels[x, y] = mandelbrot_sequence((x/(500/4))-2,(y/(500/4))-2)


  
# to display the created fractal after  
# completing the given number of iterations 
img.show() 


        


