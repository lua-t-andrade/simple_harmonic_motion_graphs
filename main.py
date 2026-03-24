import matplotlib.pyplot as plt
import numpy as np

# Initial conditions
amplitude = 5
phi = 0
mass = 100.0
K = 25.0
angular_velocity = np.sqrt(K / mass)
total_time = 100

# Functions of movement
def displacement(time):
    return amplitude * np.cos(phi + angular_velocity * time)

def velocity(time):
    return (-1 * amplitude) * angular_velocity * np.sin(phi + angular_velocity * time)

def acceleration(time):
    return amplitude * (angular_velocity ** 2) * np.cos(phi + angular_velocity * time)

# Setting the numpy arrays
time_array = np.linspace(0, total_time, num=1000, dtype=float)
displacement_array = np.array(displacement(time_array), dtype=float)
velocity_array = np.array(velocity(time_array), dtype=float)
acceleration_array = np.array(acceleration(time_array), dtype=float)

# Important information
max_speed = amplitude * angular_velocity
max_acc = amplitude * (angular_velocity ** 2)
time_period = (2 * np.pi) / angular_velocity
total_mechanical_energy = (mass * (angular_velocity ** 2) * (amplitude ** 2)) * 0.5

# Print some important values
print(f"Maximum speed: \t{max_speed}\n")
print(f"Maximum acceleration: \t{max_acc}\n")
print(f"Time period: \t{time_period:.2f}\n")
print(f"Total mechanical energy: \t{total_mechanical_energy:.2f}\n\n")

# Setting up matplotlib for plotting the graph
fig, time_velocity = plt.subplots()
fig2, time_acceleration = plt.subplots()
fig3, time_displacement = plt.subplots()

time_velocity.plot(time_array, velocity_array)
time_acceleration.plot(time_array, acceleration_array)
time_displacement.plot(time_array, displacement_array)

time_velocity.set(xlabel='time (s)', ylabel='velocity (m/s)',
       title='Velocity graph')
time_velocity.grid()

time_acceleration.set(xlabel='time (s)', ylabel='acceleration (m/s²)',
       title='Acceleration graph')
time_acceleration.grid()

time_displacement.set(xlabel='time (s)', ylabel='displacement (m)',
       title='Displacement graph')
time_displacement.grid()

fig.savefig("v.png")
fig2.savefig("a.png")
fig3.savefig("d.png")    
