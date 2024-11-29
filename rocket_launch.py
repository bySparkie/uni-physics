# this file plots the velocity, acceleration and height of a rocket during the first stage (132 seconds)
# approximating the artemis-1 launch in 2022

import numpy as np
import matplotlib.pyplot as plt

# initialization of values; user input
mass = 2.61e6 # initial mass of the rocket in kg
burn_rate = 9000 # fuel burn rate in kg/s
velocity = 4400 # velocity of ejected fuel in m/s
g = 9.81 # gravitational acceleration of earth in m/s²

# initialization of acceleration function
def a(t):
    return -g + (velocity * burn_rate)/(mass - burn_rate * t)

def v(t):
    return -g * t - velocity * np.log(mass - burn_rate * t) + velocity * np.log(mass)

def z(t):
    return ((-velocity * ((burn_rate * t - mass) * np.log(mass - burn_rate * t) - burn_rate * t))/burn_rate) -0.5 * g * t*t + velocity * np.log(mass) * t + (velocity * (-mass * np.log(mass)))/burn_rate

t_list = np.linspace(0, 132, 100)

data = {
    'Acceleration': {'y_values': a(t_list), 'y_label': '$a$ in m/s²'},
    'Velocity': {'y_values': v(t_list), 'y_label': '$v$ in m/s'},
    'Height': {'y_values': z(t_list)/1000, 'y_label': '$z$ in km'}
}

for title, info in data.items():
    y = info['y_values']
    label = info['y_label']

    plt.figure(dpi=120)
    plt.plot(t_list, y, label=title)
    plt.title(title)
    plt.xlabel('$t$ in s')
    plt.ylabel(label)
    plt.grid(True)
    plt.savefig('plots_pngs/rocket' + title + '.png')  # uncomment to save, maybe edit file path

plt.show()