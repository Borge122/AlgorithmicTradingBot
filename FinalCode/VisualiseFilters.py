import matplotlib.pyplot as plt
import numpy as np

kernals = [
    np.array([0, 2, 1.5, 3, 1.5, 2, 0]),
    np.array([0, 1, .5, 3, .5, 1, 0]),
]


for i in range(kernals.__len__()):
    plt.subplot(f"1{kernals.__len__()}{i}")
    plt.plot(kernals[i])
plt.show()
