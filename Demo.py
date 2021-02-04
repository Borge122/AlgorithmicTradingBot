from BaseFunctions import *

test = load_stocks_20m("GBPUSD", hours_to_load=24*365, periods=(20, 50, 200))
for key in test.keys():
    print(test[key]["EMA 200"])