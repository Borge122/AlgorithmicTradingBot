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
STOCKS = ["GBPUSD"]
LOAD_DATA_FROM = dt.datetime.strptime("03/02/2021 17:00:00", "%d/%m/%Y %H:%M:%S")
phase_confidence_level = 0.5
phase_uncertainty = 0.2
load_stocks_1d(STOCKS[0], LOAD_DATA_FROM, (20, 50, 200))
raise