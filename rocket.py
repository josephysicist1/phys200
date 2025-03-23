import math
import matplotlib.pyplot as plt
import random

G = 6.67430e-11  #Gravitational Const. 
M_e = 5.972e24   #Mass of Earth(kg)
R_e = 6371e3     #Radius of Earth(m)

def gravitationalF(G, M_e, m, r) :
  return G * M_e * m / r**2
    
def netForce(thrust, Fg):
  return thrust - Fg

#SaturnV rocket properties is obtained from https://tr.wikipedia.org/wiki/Saturn_V
m0 = 2.965e6                                #Initial mass of the rocket
mf = 1.1e6                                  #Final mass after combustion
thrust = 35.1e6                             #Thrust in 1st stage(N)
burn_rate = (m0 - mf) / 168                 #Burn rate(kg/s) - 1st stage lasts 168 seconds  

#Parameters for lift off
dt = 0.1 
time = 0
v = 0 
r = R_e                                     #Initial distance is equal to the radius of Earth
m = m0                                      #Initial mass

#Storing data for plotting graphs
time_points = []
velocities = []
distances = []
masses = []
gravitational_forces = []

time_points.append(time)
velocities.append(v)
distances.append(r)
masses.append(m)
gravitational_forces.append(gravitationalF(G, M_e, m, r))

while v < math.sqrt(2 * G * M_e / r) and m > mf:

    Fgrav = gravitationalF(G, M_e, m, r)
    F_net = netForce(thrust, Fg)
    a = F_net / m
    v = v + a * dt
    r = r + v * dt
    m = m - burn_rate * dt 

    if m < mf:
        m = mf                        #instant mass can't be less than final mass

    time_points.append(time)
    velocities.append(v)
    distances.append(r)
    masses.append(m)
    gravitational_forces.append(Fgrav)

    time += dt

plt.figure(figsize=(12, 12))

plt.subplot(4, 1, 1)
plt.plot(time_points, velocities)
plt.title("Rocket Velocity vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")

plt.subplot(4, 1, 2)
plt.plot(time_points, distances)
plt.title("Rocket Distance from Earth vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Distance (m)")

plt.subplot(4, 1, 3)
plt.plot(time_points, masses)
plt.title("Rocket Mass vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Mass (kg)")

plt.subplot(4, 1, 4)
plt.plot(time_points, gravitational_forces)
plt.title("Gravitational Force Acting on the Rocket vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Gravitational Force (N)")

plt.tight_layout()
plt.show()

# FOR CHECKING THE CALCULATIONS
def calculations_check ():
  '''
  during the lift of there will be only one thing that is not going to change, which is
  G * M_e . We can obtain it from the (Gravitational Force * distance**2) / (instantaneous mass of the rocket)

  G * M_e = Fgrav * r**2 / m
  Call the function to control the changing parameters and constant ones
  '''
  for i in range(400) :
    print("t= ", time_points[i]," v=",velocities[i], " Fg=" , gravitational_forces[i], " r= ",distances[i], " mass=", masses[i], "check = ", gravitational_forces[i]*distances[i]**2 / masses[i]  )
