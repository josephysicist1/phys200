import numpy as np
import matplotlib.pyplot as plt

mu_0=4 * np.pi * 1e-7         #Magnetic constant
M=8.05e22                     #Magnetic dipole moment of the Earth - A * m**2
radius_earth=6.371e6          #Radius of Earth - meter
distance_to_moon=384400e3     #Distance to the Moon

def magnetic_field(r, theta):
    B=(mu_0 * M / (4 * np.pi * r**3)) * 2 * np.cos(theta)
    return B

trajectory_r=np.linspace(radius_earth, distance_to_moon, 1000)                #Distance from the center of Earth
trajectory_theta=np.arccos(radius_earth / trajectory_r)                       #Angle from the vertical

#Magnetic fields during flight
magnetic_fields=magnetic_field(trajectory_r, trajectory_theta)

#Time steps in arbitrary units
time_steps=np.linspace(0, 1, len(trajectory_r))

plt.figure(figsize=(10, 6))
plt.plot(time_steps, magnetic_fields * 1e9, label='Magnetic Field (nT)')        #Nanotesla is choosen for obtaining readable result 
plt.xlabel('Time Step')
plt.ylabel('Magnetic Field Strength (nT)')
plt.title('Magnetic Field Strength Along Apollo 11 Trajectory')
plt.grid(True)
plt.legend()
plt.show()