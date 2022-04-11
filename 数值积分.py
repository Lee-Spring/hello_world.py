# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 21:30:58 2022

@author: 27976
"""

import numpy as np
import matplotlib.pyplot as plt
import random

x = []
y = []
for i in range(50,100):
    i = i/100
    x.append(i)
    y.append(1/np.sin(1/i))
#plt.plot(x,y)
count = 0
for i in range(1000000):
    x = random.uniform(0.5,1.0)
    y = random.uniform(0,1.2)
    if y<= 1/np.sin(1/x):
        count += 1

s = 0.5*1.2*count/1000000
print(s)

def f(x):
    y = 1/np.sin(1/x)
    return y
a = 0.5
b = 1.0
s1 = (b-a)*(f(a)+4*f((a+b)/2)+f(b))/6
print (s1)

s2 = 0
for i in range(1000001):
    h = (b-a)/1000000
    s2 += f(a+i*h)*h
print(s2)