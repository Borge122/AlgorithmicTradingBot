
from BaseFunctions import *


a = load_stocks_1h("GBPUSD", dt.datetime.strptime("01/01/2021 0:00:00", "%d/%m/%Y %H:%M:%S"), (5, 20, 50, 200))
print(list(np.round([a[key]["EMA 5"] for key in a.keys()][610:628], 5)))
plt.show()
#info = load_stocks_1h("XAGUSD", dt.datetime.strptime("08/02/2021 0:00:00", "%d/%m/%Y %H:%M:%S"), (20, 50, 200))
#plt.plot([info[key]["CLOSE"] for key in sorted(info.keys())[8:21]])
#plt.show()
#print([info[key]["CLOSE"] for key in sorted(info.keys())[8:21]])
kernals = [
    np.array([[1.37183, 1.37092, 1.37005, 1.36967, 1.3696, 1.37061, 1.37171, 1.37238, 1.37295, 1.37327, 1.37361, 1.3738, 1.37385, 1.37371, 1.37396, 1.3744, 1.37483, 1.37594]]),
    np.array([0.97791, 0.97892, 0.97976, 0.98104, 0.98316, 0.98229, 0.98202, 0.98146, 0.9812, 0.9809, 0.98061, 0.98116, 0.98189, 0.983]),
np.array([27.138, 26.956, 27.025, 27.045, 27.166, 27.184, 27.364, 27.423, 27.481, 27.532, 27.45, 27.403, 27.464]),
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
