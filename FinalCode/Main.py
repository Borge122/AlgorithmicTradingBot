import Orders, BaseFunctions, MetaTrader5 as mt5

account = 123456;
password = "A1b2C3!ksdlhg"

if not mt5.initialize():
    print(mt5.last_error())
    return 1
if not mt5.login(account, password):
    print(mt5.last_error())
    return 1

symbols = {"EURGBP": [], "GBPUSD": [], "EURUSD": []}

mt5.symbol_select("EURGBP", true)
mt5.symbol_select("GBPUSD", true)
mt5.symbol_select("EURUSD", true)

def algorithm():
    return {"EURGBP": [random.getrandbits(2)), bool(random.getrandbits(1))], "GBPUSD": [random.getrandbits(2)), bool(random.getrandbits(1))], "EURUSD": [random.getrandbits(2)), bool(random.getrandbits(1))]}

items = algorithm();
for symbol in items:
    if items[symbol][0] == 0:
        symbols[symbol].append(Orders.buy(symbol, 0.01))
    if items[symbol][0] == 1:
        symbols[symbol].append(Orders.sell(symbol, 0.01))
    if items[symbol][1] == True:
        for order in symbols[symbol]:
            Order.close(order)

mt5.shutdown();
