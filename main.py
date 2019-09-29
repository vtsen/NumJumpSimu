# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 15:26:58 2019

@author: Zhen
"""

import numpy as np
from matplotlib import pyplot as plt

MAX_STEP = 10000
N_TRIAL = 10
BLOW_UP = 1E4
EPS = 1E-5

def diverge(array):
    return max(array) > BLOW_UP

def converge(array):
    return max(array) - min(array) < EPS

plt.figure(figsize=[10,10])
legend=[]
for n in [2,3,4,5]:#,10,30,100]:
    print(n)
    xs = np.arange(0.5, 1.1, 0.05)
    ys = []
    for mult in xs:
        print(mult)
        upper_bound = 0
        for i_trial in range(N_TRIAL):
            points = np.random.rand(n)
            step = 0
            while not diverge(points) and not converge(points) and step < MAX_STEP:
                points = np.sort(points)
                index_mover = np.random.randint(0, n-1)
                points[index_mover] = points[index_mover+1] + mult*(points[index_mover+1]-points[index_mover])
                step += 1
            upper_bound += max(points)
            print(step, diverge(points), converge(points))
        upper_bound /= N_TRIAL
        ys.append(upper_bound)
    plt.plot(xs, ys)
    legend.append("N={}".format(n))
plt.legend(legend)
plt.show()
plt.close()