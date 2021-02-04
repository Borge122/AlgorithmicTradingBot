from BaseFunctions import *

'''-----------------------------------------------'''
'''PARAMETERS'''
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
STOCKS = ["GBPUSD"]
HOURS_TO_LOAD = 24*30
phase_confidence_level = 0.5
phase_confidence_uncertainty = 0.2
'''-----------------------------------------------'''
phase_filters = [
    np.array([1, 3, 2, 4]),
    np.array([0, 3, 2, 5]),
    np.array([0, 1, 2, 1, 2]),
    np.array([-1, 1, 2, 1, 2]),
    np.array([0, 3, 2])
]
phase_filters = [normalise(kernal) for kernal in phase_filters]

LATEST_STOCK_DATA = {}
for stock in STOCKS:
    LATEST_STOCK_DATA[stock] = load_stocks(stock, HOURS_TO_LOAD, (20, 50, 200))
    convolution_result = conv_1d([LATEST_STOCK_DATA[stock][key]["CLOSE"] for key in sorted(LATEST_STOCK_DATA[stock].keys())], phase_filters, phase_confidence_level, phase_confidence_uncertainty)
    for i in range(len(LATEST_STOCK_DATA[stock].keys())):
        key = sorted(LATEST_STOCK_DATA[stock].keys())[i]
        LATEST_STOCK_DATA[stock][key]["PHASE_CONV"] = convolution_result[i]

        if LATEST_STOCK_DATA[stock][key]["EMA 20"] < LATEST_STOCK_DATA[stock][key]["EMA 50"] < LATEST_STOCK_DATA[stock][key]["EMA 200"]:
            LATEST_STOCK_DATA[stock][key]["STACKING_ORDER"] = "Negative"
        elif LATEST_STOCK_DATA[stock][key]["EMA 20"] > LATEST_STOCK_DATA[stock][key]["EMA 50"] > LATEST_STOCK_DATA[stock][key]["EMA 200"]:
            LATEST_STOCK_DATA[stock][key]["STACKING_ORDER"] = "Positive"
        else:
            LATEST_STOCK_DATA[stock][key]["STACKING_ORDER"] = False


for i in range(len(LATEST_STOCK_DATA[STOCKS[0]].keys())-1):
    key = sorted(LATEST_STOCK_DATA[STOCKS[0]].keys())
    if checker(LATEST_STOCK_DATA[STOCKS[0]][key[i]]) == "Positive":
        plt.plot([i, i+1], [LATEST_STOCK_DATA[STOCKS[0]][key[i]]["CLOSE"], LATEST_STOCK_DATA[STOCKS[0]][key[i+1]]["CLOSE"]], c=colouriser("Positive"))
    elif checker(LATEST_STOCK_DATA[STOCKS[0]][key[i]]) == "Negative":
        plt.plot([i, i + 1], [LATEST_STOCK_DATA[STOCKS[0]][key[i]]["CLOSE"], LATEST_STOCK_DATA[STOCKS[0]][key[i + 1]]["CLOSE"]], c=colouriser("Negative"))
    else:
        plt.plot([i, i + 1], [LATEST_STOCK_DATA[STOCKS[0]][key[i]]["CLOSE"], LATEST_STOCK_DATA[STOCKS[0]][key[i + 1]]["CLOSE"]], c=colouriser(False))


#plt.plot([LATEST_STOCK_DATA[STOCKS[0]][key]["EMA 20"] for key in LATEST_STOCK_DATA[STOCKS[0]].keys()])
#plt.plot([LATEST_STOCK_DATA[STOCKS[0]][key]["EMA 50"] for key in LATEST_STOCK_DATA[STOCKS[0]].keys()])
#plt.plot([LATEST_STOCK_DATA[STOCKS[0]][key]["EMA 200"] for key in LATEST_STOCK_DATA[STOCKS[0]].keys()])
plt.show()