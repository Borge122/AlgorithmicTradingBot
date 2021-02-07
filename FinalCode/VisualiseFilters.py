import matplotlib.pyplot as plt
import numpy as np

kernals = [
    np.array([-1, 0.75, 1.75, 2, 0.5, 2]),
    #np.array([-1, 0, 1, 2, 0.5, 1]),
    #np.array([0, 0.25, 0.5, 2, 1, 1.5]),
    #np.array([0, 1, 0.5, 0.75]),
]


phase_filters = [
    np.array([0, 0.5, 1, 0, 1]),
    np.array([0, 2, 1, 3]),
    np.array([1, 2, 3, 2, 3]),
    np.array([1, 2.5, 3, 2, 2, 3.5]),
    np.array([0, 0.5, 1, 3, 2, 4]),
    np.array([0, 1, 2, 3, 2, 4]),
    np.array([-1, 1, 2, 1, 2]),
]

for i in range(kernals.__len__()):
    plt.subplot(f"1{kernals.__len__()}{i}")
    plt.plot(kernals[i])
plt.show()
