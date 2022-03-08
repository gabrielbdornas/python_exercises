# Libraries need to be installed
# Insert them in requirements.txt file
import matplotlib.pyplot as plt
import numpy as np

# Matrices and images
M = np.random.randint(0,10, size=(4,5))
print(M)

# Create an 'X' that goes at the center of the M graph
plt.imshow(M)
plt.plot([-0.5, 4.5], [-0.5, 3.5], label='first line')
plt.plot([-0.5, 4.5], [3.5, -0.5], label='second line')
plt.legend()
plt.show()
