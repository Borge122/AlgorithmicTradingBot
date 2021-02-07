from BaseFunctions import *

STOCKS = [
    ".WTICrude",
    "DE30Index",
    "UK100Index",
    "US500Index",
    "XAUUSD",
    "USDCAD",
    "AUDUSD",
    "EURUSD",
    "GBPUSD",
    "USDCHF",
    "USDJPY",
    "NZDUSD",
    "EURGBP",
    "EURAUD",
    "GBPCAD",
    "CADJPY",
    "GBPCHF",
    "AUDJPY",
    "AUDCAD",
    "EURJPY",
]


def create_dataset(from_time, to_time):
    datasets = {}
    t = from_time - dt.timedelta(seconds=from_time.second, microseconds=from_time.microsecond,)

    times = {t: np.zeros((len(STOCKS)))}
    while t <= to_time:
        t += dt.timedelta(minutes=1)
        times[t] = np.zeros((len(STOCKS)))

    for i in range(len(STOCKS)):
        stock = STOCKS[i]
        datasets[stock] = load_stocks_1m(stock, from_time, to_time, [],)
        for key in datasets[stock].keys():
            if key in times.keys():
                times[key][i] = datasets[stock][key]["CLOSE"]
    dataset = np.empty((len(STOCKS)))
    for time in sorted(times.keys()):
        dataset = np.vstack([dataset, times[time]])
    return dataset