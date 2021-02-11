
from BaseFunctions import *


#info = load_stocks_1h("XAGUSD", dt.datetime.strptime("08/02/2021 0:00:00", "%d/%m/%Y %H:%M:%S"), (20, 50, 200))
#plt.plot([info[key]["CLOSE"] for key in sorted(info.keys())[8:21]])
#plt.show()
#print([info[key]["CLOSE"] for key in sorted(info.keys())[8:21]])
kernals = [
    #np.array([0.97791, 0.97892, 0.97976, 0.98104, 0.98316, 0.98229, 0.98202, 0.98146, 0.9812, 0.9809, 0.98061, 0.98116, 0.98189, 0.983]),
    np.array([0.23372227, -0.00869702, -0.20335379, 0.37613973, -0.01257898, 0.26674747,0.3294659, -0.054754,  -0.48607448, 0.53470767 -3.00064,  0.3983263, -0.0046302,  0.9006639,  0.6625896,  0.619903,  -0.09061008, -0.32426926, -0.5682048, -0.3784316,  0.80934125])
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
