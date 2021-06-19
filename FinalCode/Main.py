import MetaTrader5 as mt5
import random
import FinalCode.Orders as Orders

account = 820585
password = "29Lf9IT6"

if not mt5.initialize():
    print(mt5.last_error())
    raise ValueError("Error! Did not initialise")
if not mt5.login(account, password=password):
    print(mt5.last_error())
    raise ValueError("Error! Did not login")

symbols = {"EURGBP": [], "GBPUSD": [], "EURUSD": []}

mt5.symbol_select("EURGBP", True)
mt5.symbol_select("GBPUSD", True)
mt5.symbol_select("EURUSD", True)


def algorithm():
    return {"EURGBP": [random.randint(2), [True, False][random.randint(2)]],
            "GBPUSD": [random.randint(2), [True, False][random.randint(2)]],
            "EURUSD": [random.randint(2), [True, False][random.randint(2)]]}


items = algorithm()
for symbol in items:
    if items[symbol][0] == 0:
        symbols[symbol].append(Orders.buy(symbol, 0.01))
    if items[symbol][0] == 1:
        symbols[symbol].append(Orders.sell(symbol, 0.01))
    if items[symbol][1]:
        for order in symbols[symbol]:
            Orders.close(order)

mt5.shutdown()
