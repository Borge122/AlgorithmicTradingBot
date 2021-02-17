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
LOAD_DATA_FROM = dt.datetime.strptime("01/01/2021 0:00:00", "%d/%m/%Y %H:%M:%S")
phase_confidence_level = 0.75
phase_uncertainty = 2
std_bounce = 5
'''-----------------------------------------------'''
phase_filters = [
    #np.array([0.97791, 0.97892, 0.97976, 0.98104, 0.98316, 0.98229, 0.98202, 0.98146, 0.9812, 0.9809, 0.98061, 0.98116, 0.98189, 0.983]),
    #np.array([27.138, 26.956, 27.025, 27.045, 27.166, 27.184, 27.364, 27.423, 27.481, 27.532, 27.45, 27.403, 27.464]),
    #np.array([1.37183, 1.37092, 1.37005, 1.36967, 1.3696, 1.37061, 1.37171, 1.37238, 1.37295, 1.37327, 1.37361, 1.3738, 1.37385, 1.37371, 1.37396, 1.3744, 1.37483, 1.37594]),
    #np.array([0.23372227, -0.00869702, -0.20335379, 0.37613973, -0.01257898, 0.26674747, 0.3294659, -0.054754, -0.48607448, 0.53470767 - 3.00064, 0.3983263, -0.0046302, 0.9006639, 0.6625896, 0.619903, -0.09061008, -0.32426926, -0.5682048,
    #          -0.3784316, 0.80934125]),

    np.array([-1, 0, 1, 2, 0.5, 1]),
    np.array([0, 0.25, 0.5, 2, 1, 1.5]),
    np.array([0, 1, 0.5, 0.75]),
]

LATEST_STOCK_DATA = {}
for stock in STOCKS:
    LATEST_STOCK_DATA[stock] = load_stocks_1h(stock, LOAD_DATA_FROM, (5, 20, 50, 200))
    LATEST_STOCK_DATA[stock] = bounce_off_20_ema(LATEST_STOCK_DATA[stock], std_bounce)
    convolution_result = conv_1d([LATEST_STOCK_DATA[stock][key]["EMA 5"] for key in sorted(LATEST_STOCK_DATA[stock].keys())], phase_filters)
    list_of_significant_convolutions = convolutional_significance(convolution_result, phase_confidence_level, phase_uncertainty)

    for i in range(len(LATEST_STOCK_DATA[stock].keys())):
        key = sorted(LATEST_STOCK_DATA[stock].keys())[i]
        LATEST_STOCK_DATA[stock][key]["PHASE_CONV"] = list_of_significant_convolutions[i]

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

plt.plot([LATEST_STOCK_DATA[STOCKS[0]][key]["EMA 5"] for key in LATEST_STOCK_DATA[STOCKS[0]].keys()])
plt.plot([LATEST_STOCK_DATA[STOCKS[0]][key]["EMA 20"] for key in LATEST_STOCK_DATA[STOCKS[0]].keys()])
plt.plot([LATEST_STOCK_DATA[STOCKS[0]][key]["EMA 50"] for key in LATEST_STOCK_DATA[STOCKS[0]].keys()])
plt.plot([LATEST_STOCK_DATA[STOCKS[0]][key]["EMA 200"] for key in LATEST_STOCK_DATA[STOCKS[0]].keys()])
plt.show()