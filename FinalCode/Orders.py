import MetaTrader5 as mt5


class Order:
    def __init__(self, order, request):
        self.request = request
        self.result = order


def buy(stock_name, volume):
    """
    Buy stock. Note, you must login with mt5.login(accountNo, password) prior to this
    For this function to work, you must also enable autotrading by pressing the "Algo trading" button
    :param stock_name: The symbol code
    :param volume: Volume in lots. E.g. 0.01 is 1k dollars in GBPUSD
    :return: class Order
    """
    symbol_info = mt5.symbol_info(stock_name)
    if symbol_info is None or not symbol_info.visible:
        return False

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "type": mt5.ORDER_TYPE_BUY,
        "symbol": stock_name,
        "volume": volume,
        "price": mt5.symbol_info_tick(stock_name).ask
    }
    return Order(mt5.order_send(request), request)


def sell(stock_name, volume):
    """
    Buy stock. Note, you must login with mt5.login(accountNo, password) prior to this
    For this function to work, you must also enable autotrading by pressing the "Algo trading" button
    :param stock_name: The symbol code
    :param volume: Volume in lots. E.g. 0.01 is 1k dollars in GBPUSD
    :return: class Order
    """
    symbol_info = mt5.symbol_info(stock_name)
    if symbol_info is None or not symbol_info.visible:
        return False

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "type": mt5.ORDER_TYPE_SELL,
        "symbol": stock_name,
        "volume": volume,
        "price": mt5.symbol_info_tick(stock_name).ask
    }
    return Order(mt5.order_send(request), request)

def close_trade(order):
    """
    Improved version of stolen stackoverflow code. Closes a trade order
    :param order: class Order
    :return: class Order
    """
    if order.request["type"] == mt5.ORDER_TYPE_SELL:
        trade_type = mt5.ORDER_TYPE_BUY
        price = mt5.symbol_info_tick(order.request['symbol']).ask
    elif order.request["type"] == mt5.ORDER_TYPE_BUY:
        trade_type = mt5.ORDER_TYPE_SELL
        price = mt5.symbol_info_tick(order.request['symbol']).bid
    else:
        return None
    position_id = order.result

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": order.request['symbol'],
        "volume": order.request['volume'],
        "type": trade_type,
        "position": position_id,
        "price": price,
    }

    return Order(mt5.order_send(request), request)
