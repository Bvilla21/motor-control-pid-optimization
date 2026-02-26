import numpy as np
import matplotlib.pyplot as plt

# Simple PID simulation parameters
Kp = 1.2
Ki = 0.01
Kd = 0.5

time = np.linspace(0, 10, 100)
setpoint = 1
output = []

error_sum = 0
prev_error = 0

for t in time:
    error = setpoint - 0.5*np.sin(t)
    error_sum += error
    d_error = error - prev_error
    
    control = Kp*error + Ki*error_sum + Kd*d_error
    output.append(control)
    
    prev_error = error

plt.plot(time, output)
plt.title("PID Control Output")
plt.xlabel("Time")
plt.ylabel("Control Signal")
plt.show()
