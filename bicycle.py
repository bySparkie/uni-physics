# this file plots the function describing a bicycle slowing down from a given speed through a differential equation,
# describing the effects of friction between the tires and the ground

import numpy as np
import matplotlib.pyplot as plt

# initialization of values; user input
velocity_0 = 30 # starting velocity in km/h
mass = 75 # in kg
coefficient_drag = 0.5 # drag coefficient

# initialization of differential equation, given
def v(t):
    return (mass*velocity_0)/(coefficient_drag*t*velocity_0+mass)

t_list = np.linspace(0, 100, 100)

v_list = v(t_list)

plt.figure(num=0,dpi=120)
plt.plot(t_list, v_list, color='orange')

plt.xlabel('$t$ in s')
plt.ylabel('$v$ in km/h')
plt.title('Velocity of bicycle experiencing drag')
plt.grid(True)

plt.savefig('plots_pngs/Bicycle_drag.png') # uncomment to save, maybe edit file path

plt.show()
