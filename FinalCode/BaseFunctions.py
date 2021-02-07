import MetaTrader5 as mt5
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt


def load_stocks_1d(stock_name, load_from_datetime, ema_periods=(20, 50, 200)):
    '''
    Loads daily stock data.
    :param stock_name: The symbol code, e.g. AUDUSD
    :param load_from_datetime: This should be a datetime value e.g. dt.datetime.strptime("07/02/2020 15:00:00", "%d/%m/%Y %H:%M:%S")
    :param ema_periods: A tuple indicating the periods for which EMA should be calculated.
    :return: Returns a dictionary indexed by time. Each index is then a further dictionary see {dictionary}.keys() for more details
    '''

    mt5.initialize()
    stock_data = mt5.copy_rates_range(stock_name, mt5.TIMEFRAME_D1, load_from_datetime, dt.datetime.now())
    dataset = {}

    for datapoint in stock_data:
        dataset[dt.datetime.utcfromtimestamp(datapoint[0])] = {"OPEN": datapoint[1], "HIGH": datapoint[2], "LOW": datapoint[3], "CLOSE": datapoint[4], "VOLUME": datapoint[5], "SPREAD": datapoint[6]}
    mt5.shutdown()
    for period in ema_periods:
        dataset = exponential_moving_average(dataset, period)
    return dataset


def load_stocks_4h(stock_name, load_from_datetime, ema_periods=(20, 50, 200)):
    '''
    Loads 4-hourly stock data.
    :param stock_name: The symbol code, e.g. AUDUSD
    :param load_from_datetime: This should be a datetime value e.g. dt.datetime.strptime("07/02/2020 15:00:00", "%d/%m/%Y %H:%M:%S")
    :param ema_periods: A tuple indicating the periods for which EMA should be calculated.
    :return: Returns a dictionary indexed by time. Each index is then a further dictionary see {dictionary}.keys() for more details
    '''

    mt5.initialize()
    stock_data = mt5.copy_rates_range(stock_name, mt5.TIMEFRAME_H4, load_from_datetime, dt.datetime.now())
    dataset = {}

    for datapoint in stock_data:
        dataset[dt.datetime.utcfromtimestamp(datapoint[0])] = {"OPEN": datapoint[1], "HIGH": datapoint[2], "LOW": datapoint[3], "CLOSE": datapoint[4], "VOLUME": datapoint[5], "SPREAD": datapoint[6]}
    mt5.shutdown()
    for period in ema_periods:
        dataset = exponential_moving_average(dataset, period)
    return dataset


def load_stocks_4h(stock_name, load_from_datetime, ema_periods=(20, 50, 200)):
    '''
    Loads 4-hourly stock data.
    :param stock_name: The symbol code, e.g. AUDUSD
    :param load_from_datetime: This should be a datetime value e.g. dt.datetime.strptime("07/02/2020 15:00:00", "%d/%m/%Y %H:%M:%S")
    :param ema_periods: A tuple indicating the periods for which EMA should be calculated.
    :return: Returns a dictionary indexed by time. Each index is then a further dictionary see {dictionary}.keys() for more details
    '''

    mt5.initialize()
    stock_data = mt5.copy_rates_range(stock_name, mt5.TIMEFRAME_H4, load_from_datetime, dt.datetime.now())
    dataset = {}

    for datapoint in stock_data:
        dataset[dt.datetime.utcfromtimestamp(datapoint[0])] = {"OPEN": datapoint[1], "HIGH": datapoint[2], "LOW": datapoint[3], "CLOSE": datapoint[4], "VOLUME": datapoint[5], "SPREAD": datapoint[6]}
    mt5.shutdown()
    for period in ema_periods:
        dataset = exponential_moving_average(dataset, period)
    return dataset


def load_stocks_1h(stock_name, load_from_datetime, ema_periods=(20, 50, 200)):
    '''
    Loads hourly stock data.
    :param stock_name: The symbol code, e.g. AUDUSD
    :param load_from_datetime: This should be a datetime value e.g. dt.datetime.strptime("07/02/2020 15:00:00", "%d/%m/%Y %H:%M:%S")
    :param ema_periods: A tuple indicating the periods for which EMA should be calculated.
    :return: Returns a dictionary indexed by time. Each index is then a further dictionary see {dictionary}.keys() for more details
    '''

    mt5.initialize()
    stock_data = mt5.copy_rates_range(stock_name, mt5.TIMEFRAME_H1, load_from_datetime, dt.datetime.now())
    dataset = {}

    for datapoint in stock_data:
        dataset[dt.datetime.utcfromtimestamp(datapoint[0])] = {"OPEN": datapoint[1], "HIGH": datapoint[2], "LOW": datapoint[3], "CLOSE": datapoint[4], "VOLUME": datapoint[5], "SPREAD": datapoint[6]}
    mt5.shutdown()
    for period in ema_periods:
        dataset = exponential_moving_average(dataset, period)
    return dataset


def load_stocks_20m(stock_name, load_from_datetime, ema_periods=(20, 50, 200)):
    '''
    Loads 20-minutely stock data.
    :param stock_name: The symbol code, e.g. AUDUSD
    :param load_from_datetime: This should be a datetime value e.g. dt.datetime.strptime("07/02/2020 15:00:00", "%d/%m/%Y %H:%M:%S")
    :param ema_periods: A tuple indicating the periods for which EMA should be calculated.
    :return: Returns a dictionary indexed by time. Each index is then a further dictionary see {dictionary}.keys() for more details
    '''

    mt5.initialize()
    stock_data = mt5.copy_rates_range(stock_name, mt5.TIMEFRAME_M20, load_from_datetime, dt.datetime.now())
    dataset = {}

    for datapoint in stock_data:
        dataset[dt.datetime.utcfromtimestamp(datapoint[0])] = {"OPEN": datapoint[1], "HIGH": datapoint[2], "LOW": datapoint[3], "CLOSE": datapoint[4], "VOLUME": datapoint[5], "SPREAD": datapoint[6]}
    mt5.shutdown()
    for period in ema_periods:
        dataset = exponential_moving_average(dataset, period)
    return dataset


def normalise(x):
    '''
    Normalises a list x.
    :param x: A list
    :return: A normalised list with mean zero, standard deviation 1. Unless the original list had a standard deviation of zero, in this case it remains zero
    '''
    x = np.array(x)
    if np.std(x) == 0:
        return np.subtract(x, np.mean(x))
    else:
        return np.divide(np.subtract(x, np.mean(x)), np.std(x))


def conv_1d(x, kernals):
    '''
    Performs a one dimensional discrete convolution. Applied retrospectively
    :param x: The list of data to be convolved.
    :param kernals: The filter(s) to be used in the convolution. These should be numpy arrays in a list [filter1, filter2... ]
    :return: A list of convolved results for each filter.
    '''
    kernals = [normalise(kernal) for kernal in kernals]
    lists = []
    for kernal in kernals:
        convolved_result = [np.mean(np.multiply(normalise(x[i - kernal.__len__():i]), kernal)) for i in range(kernal.__len__(), x.__len__())]
        lists.append([0 for i in range(kernal.__len__())] + convolved_result)
    return lists


def convolutional_significance(convolved_result, confidence_level, confidence_uncertainty):
    '''
    This functions checks the result of a convolution to see whether any results are of significant interest.
    The convolution returns a value between -1 and 1. -1 is equivalent to 100% certainty the opposite pattern is present, 1 is equivalent to 100% certainty
    the selected pattern is present. Whilst 0% is neither pattern is present. If the largest absolute certainty is greater than the confidence_level and the
    standard deviation of uncertainties is below the confidence_uncertainty then it is deemed as a significant finding.
    :param convolved_result: A list containing numbers as a result of convolution.
    :param confidence_level: The minimum confidence percentage to deem a finding as significant
    :param confidence_uncertainty: The maximum range of standard deviation in the detection to deem as significant.
    :return: A list, where "Positive" a significant pattern was detected, "Negative" a inverted significant pattern was detected and "False" if no pattern was detected.
    '''
    convolved_result = np.array(convolved_result)
    absoluted_argmax, deviation = np.argmax(np.abs(convolved_result), axis=0), np.std(convolved_result, axis=0)
    listed = []
    for i in range(absoluted_argmax.shape[0]):
        if abs(convolved_result[absoluted_argmax[i], i]) >= confidence_level and deviation[i] <= confidence_uncertainty:

            if np.sign(convolved_result[absoluted_argmax[i], i]) == 1:
                listed.append("Positive")
            elif np.sign(convolved_result[absoluted_argmax[i], i]) == -1:
                listed.append("Negative")
            else:
                raise ValueError("Positive nor Negative found!")
        else:
            listed.append(False)
    return listed


def exponential_moving_average(dataset, period):
    """Do not use this function in standard code. It is designed only for the load_stocks_{} module(s)."""
    k = 2 / (period + 1)

    for i in range(len(dataset.keys())):
        key = sorted(dataset.keys())[i]
        if i == 0:
            dataset[key]["EMA {0}".format(period)] = dataset[key]["CLOSE"]
        else:
            dataset[key]["EMA {0}".format(period)] = dataset[key]["CLOSE"]*k + dataset[sorted(dataset.keys())[i-1]]["EMA {0}".format(period)]*(1-k)
    return dataset


def colouriser(x):
    '''
    Returns RGB colours for a value of significances.
    :param x: Value of significances.
    :return: RGB colour.
    '''
    if x == "Positive":
        return [0, 1, 0]
    elif x == "Negative":
        return [1, 0, 0]
    else:
        return [0, 0, 0]


def checker(x):
    '''Checks multiple values of signifcance to see whether their is agreement.'''
    if x["PHASE_CONV"] == x["STACKING_ORDER"] == "Positive" and x["BOUNCE"]:
        return "Positive"
    elif x["PHASE_CONV"] == x["STACKING_ORDER"] == "Negative" and x["BOUNCE"]:
        return "Negative"
    else:
        return False


def bounce_off_20_ema(dataset, below_std):
    '''
    Calculates whether the stock has bounced off the 20 EMA line.
    :param dataset: Stock data from load_stock_{} module(s)
    :param below_std: The difference is normalised, then those which fall under below_std are registered as a bounce
    :return: The same dataset but with a new key for bounces (True or False)
    '''
    listed = []
    for key in sorted(dataset.keys()):
        if "EMA 20" in dataset[key].keys():
            listed.append(dataset[key]["CLOSE"] - dataset[key]["EMA 20"])
        else:
            raise ValueError("To use this function, please ensure the 20 EMA period is calculated.")
    listed = normalise(np.array(listed))
    bounces = np.zeros_like(listed)
    bounces[np.where(abs(listed) < below_std)] += 1

    for i in range(len(dataset.keys())):
        key = sorted(dataset.keys())[i]
        if bounces[i] == 1:
            dataset[key]["BOUNCE"] = True
        elif bounces[i] == 0:
            dataset[key]["BOUNCE"] = False
        else:
            raise ValueError("Something went wrong!")
    return dataset
