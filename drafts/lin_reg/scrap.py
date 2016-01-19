import numpy as np
import matplotlib.pyplot as plt
import cmath
import csv

from matplotlib import rc
from pylab import *
from scipy.optimize import fsolve
from mpl_toolkits.axes_grid.axislines import SubplotZero

import matplotlib.cm as cm
from matplotlib.colors import LogNorm




intercept = -0.3
slope = 1.7
num_rand_var = 100
rand_var = np.empty((num_rand_var, 1))

rand_data = np.zeros((num_rand_var, 2))


for i in range(num_rand_var):
	rand_x = 1.5-3*random()
	rand_data[i,0] = rand_x

	rand_data[i,1] = intercept + slope*rand_x + rand_offset

x1 = -3
y1 = intercept + x1*slope

x2 = 3
y2 = intercept + x2*slope


plt.plot(x1, y1, x2, y2, lw = 1, ls = '--')
plt.scatter(rand_data[:,0], rand_data[:,1])

plt.show()