import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *

data = np.loadtxt("Data_Project_2.csv", delimiter=",", dtype=str)
# data should be an np array. Write a temporary line of code that
# prints the first row of the array to check that this worked.

x = data[1:, 0].astype(np.float32) # I did this one for you
y = data[1:, 1].astype(np.float32)

print("y=",y)
print("x=",x)

params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]
fig = plt.figure()
plt.scatter(x,y)
plt.plot(x,linear(x,slope,intercept),label='linear fit')
plt.xlabel('mass/g')
plt.ylabel('height/mm')
plt.show()

print_equation(slope,intercept,'g','mm')
fig.savefig('dataplot.png') # Please use this command to save your plots as PNG files
