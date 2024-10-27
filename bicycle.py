# this file plots the function describing a bicycle slowing down from a given speed through a differential equation,
# describing the effects of friction between the tires and the ground

import numpy as np
import matplotlib.pyplot as plt

# initialization of values; user input
v_0 = 30 # starting velocity in km/h
m = 75 # mass in kg
c = 0.5 # drag coefficient

# initialization of differential equation, given
def v(t):
    return m/(c*t+(m/v_0))

t_list = np.arange(0, 100, .1)

v_list = v(t_list)

plt.figure(num=0,dpi=120)
plt.plot(t_list, v_list, color='orange')

plt.xlabel('$t$ in s')
plt.ylabel('$v$ in km/h')
plt.title('Velocity of bicycle experiencing drag')

plt.savefig('plots_pngs/Bicycle_drag.png') # uncomment to save, maybe edit file path

plt.show()
