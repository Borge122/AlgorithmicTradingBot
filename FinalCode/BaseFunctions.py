import MetaTrader5 as mt5
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt


def load_stocks(stock_name, hours_to_load=12, periods=(20, 50, 200)):
    mt5.initialize()
    stock_data = mt5.copy_rates_range(stock_name, mt5.TIMEFRAME_M20, dt.datetime.now() - dt.timedelta(hours=hours_to_load), dt.datetime.now())

    dataset = {}
    t = dt.datetime.now() - dt.timedelta(hours=hours_to_load)
    t = t - dt.timedelta(minutes=t.minute % 20, seconds=t.second, microseconds=t.microsecond)
    while t <= dt.datetime.now():
        dataset[t] = {}
        t += dt.timedelta(minutes=20)

    for stock in stock_data:
        time = dt.datetime.utcfromtimestamp(stock[0])
        if time in dataset.keys():
            dataset[time] = {"OPEN": stock[1], "HIGH": stock[2], "LOW": stock[3], "CLOSE": stock[4], "VOLUME": stock[5], "SPREAD": stock[6], "INTERPOLATED": False}
        else:
            raise ValueError("ERROR!! Datetime {0} not found in dictionary".format(time))

    for key in dataset.keys():
        if "OPEN" not in dataset[key].keys():
            if key - dt.timedelta(minutes=20) in dataset.keys():
                dataset[key] = dataset[key - dt.timedelta(minutes=20)].copy()
                dataset[key]["INTERPOLATED"] = True
            elif key + dt.timedelta(minutes=20) in dataset.keys():
                dataset[key] = dataset[key + dt.timedelta(minutes=20)].copy()
                dataset[key]["INTERPOLATED"] = True
    mt5.shutdown()
    for period in periods:
        dataset = exponential_moving_average(dataset, period)
    return dataset


def normalise(x):
    x = np.array(x)
    return np.divide(np.subtract(x, np.mean(x)), np.std(x))


def conv_1d(x, kernals, confidence_level, confidence_uncertainty):
    lists = []
    for kernal in kernals:
        convolved_result = [np.mean(np.multiply(normalise(x[i - kernal.__len__():i]), kernal)) for i in range(kernal.__len__(), x.__len__())]
        lists.append([0 for i in range(kernal.__len__())] + convolved_result)
    level, deviation = np.mean(np.array(lists), axis=0), np.std(np.array(lists), axis=0)
    listed = []
    for i in range(level.shape[0]):
        print(f"{level[i]:3.2f}, {deviation[i]:3.2f}")
        if abs(level[i]) >= confidence_level and deviation[i] <= confidence_uncertainty:
            if np.sign(level[i]) == 1:
                listed.append("Positive")
            elif np.sign(level[i]) == -1:
                listed.append("Negative")
            else:
                raise ValueError("Positive nor Negative found!")
        else:
            listed.append(False)
    return listed


def exponential_moving_average(dataset, period):
    k = 2 / (period + 1)
    for key in sorted(dataset.keys()):
        if key == min(dataset.keys()):
            dataset[key]["EMA {0}".format(period)] = dataset[key]["CLOSE"]
        else:
            dataset[key]["EMA {0}".format(period)] = dataset[key]["CLOSE"]*k + dataset[key-dt.timedelta(minutes=20)]["EMA {0}".format(period)]*(1-k)
    return dataset

