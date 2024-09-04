import numpy as np
import matplotlib.pyplot as plt

yy, zz = np.meshgrid(range(2), range(2))
xx = yy*0

print(yy)

ax = plt.subplot(projection='3d')
ax.plot_surface(xx, yy, zz, color="#ff0000")
plt.show()
