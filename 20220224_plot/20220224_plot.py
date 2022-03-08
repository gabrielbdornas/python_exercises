# Libraries need to be installed
# Insert them in requirements.txt file
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-9,10)
y = x**2
print(x)
print(y)
# x and y are numpy.ndarray class
print(type(x))
print(type(y))

# r - red
# g - green
plt.plot(x,y,'r') # red line
plt.plot(x,y/2, 'gs') # green circles
# plt.show isn't needed in jupyter notbook but here it is.
plt.show()

# Create a line
plt.plot([0,3], [-1,1], label='first line')
plt.plot([-2,0], [-4,1], label='second line')
plt.legend()
plt.show()
