from collections import deque
import time
import random
from abc import ABC

from enum import Enum


class OrderType(Enum):
    LIMIT = 1
    MARKET = 2
    IOC = 3


class OrderSide(Enum):
    BUY = 1
    SELL = 2


class NonPositiveQuantity(Exception):
    pass


class NonPositivePrice(Exception):
    pass


class InvalidSide(Exception):
    pass


class UndefinedOrderType(Exception):
    pass


class UndefinedOrderSide(Exception):
    pass


class NewQuantityNotSmaller(Exception):
    pass


class UndefinedTraderAction(Exception):
    pass


class UndefinedResponse(Exception):
    pass


class Order(ABC):
    def __init__(self, id, symbol, quantity, side, time):
        self.id = id
        self.symbol = symbol
        if quantity > 0:
            self.quantity = quantity
        else:
            raise NonPositiveQuantity("Quantity Must Be Positive!")
        if side in [OrderSide.BUY, OrderSide.SELL]:
            self.side = side
        else:
            raise InvalidSide("Side Must Be Either \"Buy\" or \"OrderSide.SELL\"!")
        self.time = time


class LimitOrder(Order):
    def __init__(self, id, symbol, quantity, price, side, time):
        super().__init__(id, symbol, quantity, side, time)
        if price > 0:
            self.price = price
        else:
            raise NonPositivePrice("Price Must Be Positive!")
        self.type = OrderType.LIMIT


class MarketOrder(Order):
    def __init__(self, id, symbol, quantity, side, time):
        super().__init__(id, symbol, quantity, side, time)
        self.type = OrderType.MARKET


class IOCOrder(Order):
    def __init__(self, id, symbol, quantity, price, side, time):
        super().__init__(id, symbol, quantity, side, time)
        if price > 0:
            self.price = price
        else:
            raise NonPositivePrice("Price Must Be Positive!")
        self.type = OrderType.IOC


class FilledOrder(Order):
    def __init__(self, id, symbol, quantity, price, side, time, limit=False):
        super().__init__(id, symbol, quantity, side, time)
        self.price = price
        self.limit = limit


trader_to_exchange = deque()
exchange_to_trader = [deque() for _ in range(100)]


# Above you are given two deques where the orders submitted to the exchange and back to the trader
# are expected to be populated by the trading exchange simulator
# The first is trader_to_exchange, a deque of orders to be populated for the exchange to execute
# The second is a list of 100 deques exchange_to_trader, which are acknowledgements from the exchange
# to each of the 100 traders for trades executed on their behalf

# Below you have an implementation of a simulated thread to be used where each trader is a separate thread
class MyThread:
    list_of_threads = []

    def __init__(self, id='NoID'):
        MyThread.list_of_threads.append(self)
        self.is_started = False
        self.id = id

    def start(self):
        self.is_started = True

    def join(self):
        print('Trader ' + str(self.id) + ' will be waited')


# Paste in your implementation for the matching engine below

# ----------------------------------------------------------
# PASTE MATCHING ENGINE FROM Q2 HERE
class MatchingEngine():
    def __init__(self):
        self.bid_book = []
        self.ask_book = []
        # These are the order books you are given and expected to use for matching the orders below

    # Note: As you implement the following functions keep in mind that these enums are available:
    #     class OrderType(Enum):
    #         LIMIT = 1
    #         MARKET = 2
    #         IOC = 3

    #     class OrderSide(Enum):
    #         BUY = 1
    #         SELL = 2

    def handle_order(self, order):
        # Implement this function
        # In this function you need to call different functions from the matching engine
        # depending on the type of order you are given
        if order.type == OrderType.LIMIT:
            filled_orders = self.handle_limit_order(order)
        elif order.type == OrderType.MARKET:
            filled_orders = self.handle_market_order(order)
        elif order.type == OrderType.IOC:
            filled_orders = self.handle_ioc_order(order)
        else:
            # You need to raise the following error if the type of order is ambiguous
            raise UndefinedOrderType("Undefined Order Type!")
        return filled_orders

    def handle_limit_order(self, order):
        # Implement this function
        # Keep in mind what happens to the orders in the limit order books when orders get filled
        # or if there are no crosses from this order
        # in other words, handle_limit_order accepts an arbitrary limit order that can either be
        # filled if the limit order price crosses the book, or placed in the book. If the latter,
        # pass the order to insert_limit_order below.
        filled_orders = []
        # The orders that are filled from the market order need to be inserted into the above list
        side = order.side
        symbol = order.symbol
        if side == OrderSide.BUY:
            ask_order = [o for o in self.ask_book if o.symbol == symbol]
            if len(ask_order) == 0:
                self.insert_limit_order(order)
            else:
                if ask_order[0].price > order.price:
                    self.insert_limit_order(order)
                else:
                    #filled_id = []
                    #q = order.quantity
                    while len(self.ask_book)>0:
                        o = self.ask_book[0]
                        if o.price < order.price:
                            if order.quantity < o.quantity:
                                filled_orders.append(order)
                                filled_orders.append(LimitOrder(o.id, o.symbol, order.quantity, o.price, \
                                                                o.side, o.time))
                                self.ask_book[0].quantity = o.quantity - order.quantity
                                order.quantity = 0
                                break
                            else:
                                filled_orders.append(o)
                                order.quantity -= o.quantity
                                del self.ask_book[0]
                        else:
                            break
                    if order.quantity > 0:
                        self.insert_limit_order(order)
                        #filled_orders.append(LimitOrder(order.id,order.symbol,q-order.quantity,order.price,\
                                                        #order.side,order.time))
        elif side == OrderSide.SELL:
            bid_order = [o for o in self.bid_book if o.symbol == symbol]
            if len(bid_order) == 0:
                self.insert_limit_order(order)
            else:
                if bid_order[0].price < order.price:
                    self.insert_limit_order(order)
                else:
                    #q = order.quantity
                    while len(self.bid_book)>0:
                        o = self.bid_book[0]
                        if o.price > order.price:
                            if order.quantity < o.quantity:
                                filled_orders.append(order)
                                filled_orders.append(LimitOrder(o.id, o.symbol, order.quantity, o.price, \
                                                                o.side, o.time))
                                self.bid_book[0].quantity = o.quantity - order.quantity
                                order.quantity = 0
                                break
                            else:
                                filled_orders.append(o)
                                order.quantity -= o.quantity
                                del self.bid_book[0]
                        else:
                            break
                    if order.quantity > 0:
                        self.insert_limit_order(order)
                        #filled_orders.append(LimitOrder(order.id, order.symbol, q - order.quantity, order.price, \
                                                        #order.side, order.time))
        # The filled orders are expected to be the return variable (list)
        return filled_orders
        if order.side != OrderSide.BUY and order.side != OrderSide.SELL:
            # You need to raise the following error if the side the order is for is ambiguous
            raise UndefinedOrderSide("Undefined Order Side!")

    def handle_market_order(self, order):
        # Implement this function
        filled_orders = []
        # The orders that are filled from the market order need to be inserted into the above list
        side = order.side
        symbol = order.symbol
        if side == OrderSide.BUY:
            ask_order = [o for o in self.ask_book if o.symbol == symbol]
            if len(ask_order) > 0:
                price = ask_order[0].price
                while len(self.ask_book) > 0:
                    o = self.ask_book[0]
                    if o.price == price :
                        if order.quantity < o.quantity:
                            filled_orders.append(order)
                            filled_orders.append(LimitOrder(o.id, o.symbol, order.quantity, o.price, \
                                                            o.side, o.time))
                            self.ask_book[0].quantity = o.quantity - order.quantity
                            order.quantity = 0
                            break
                        else:
                            filled_orders.append(o)
                            order.quantity -= o.quantity
                            del self.ask_book[0]
                    else:
                        break

        elif side == OrderSide.SELL:
            bid_order = [o for o in self.bid_book if o.symbol == symbol]
            if len(bid_order) > 0:
                price = bid_order[0].price
                while len(self.bid_book) > 0:
                    o = self.bid_book[0]
                    if o.price == price:
                        if order.quantity < o.quantity:
                            filled_orders.append(order)
                            filled_orders.append(LimitOrder(o.id, o.symbol, order.quantity, o.price, \
                                                            o.side, o.time))
                            self.bid_book[0].quantity = o.quantity - order.quantity
                            order.quantity = 0
                            break
                        else:
                            filled_orders.append(o)
                            order.quantity -= o.quantity
                            del self.bid_book[0]
                    else:
                        break
        # The filled orders are expected to be the return variable (list)
        return filled_orders
        if order.side != OrderSide.BUY and order.side != OrderSide.SELL:
            # You need to raise the following error if the side the order is for is ambiguous
            raise UndefinedOrderSide("Undefined Order Side!")

    def handle_ioc_order(self, order):
        # Implement this function
        filled_orders = []
        # The orders that are filled from the ioc order need to be inserted into the above list
        side = order.side
        symbol = order.symbol
        if side == OrderSide.BUY:
            ask_order = [o for o in self.ask_book if o.symbol == symbol]
            if len(ask_order) > 0:
                while len(self.ask_book)>0:
                    o = self.ask_book[0]
                    if o.price < order.price:
                        if order.quantity < o.quantity:
                            filled_orders.append(order)
                            filled_orders.append(LimitOrder(o.id, o.symbol, order.quantity, o.price, \
                                                            o.side, o.time))
                            self.ask_book[0].quantity = o.quantity - order.quantity
                            order.quantity = 0
                            break
                        else:
                            filled_orders.append(o)
                            order.quantity -= o.quantity
                            del self.ask_book[0]
                    else:
                        break
        elif side == OrderSide.SELL:
            bid_order = [o for o in self.bid_book if o.symbol == symbol]
            if len(bid_order) > 0:
                while len(self.bid_book) > 0:
                    o = self.bid_book[0]
                    if o.price > order.price:
                        if order.quantity < o.quantity:
                            filled_orders.append(order)
                            filled_orders.append(LimitOrder(o.id, o.symbol, order.quantity, o.price, \
                                                            o.side, o.time))
                            self.bid_book[0].quantity = o.quantity - order.quantity
                            order.quantity = 0
                            break
                        else:
                            filled_orders.append(o)
                            order.quantity -= o.quantity
                            del self.bid_book[0]
                    else:
                        break
        # The filled orders are expected to be the return variable (list)
        return filled_orders
        if order.side != OrderSide.BUY and order.side != OrderSide.SELL:
            # You need to raise the following error if the side the order is for is ambiguous
            raise UndefinedOrderSide("Undefined Order Side!")

    def insert_limit_order(self, order):
        assert order.type == OrderType.LIMIT
        # Implement this function
        # this function's sole puporse is to place limit orders in the book that are guaranteed
        # to not immediately fill
        side = order.side
        if side == OrderSide.BUY:
            self.bid_book.append(order)
            self.bid_book = sorted(self.bid_book, key=lambda o: (-1 * o.price, o.time))
        elif side == OrderSide.SELL:
            self.ask_book.append(order)
            self.ask_book = sorted(self.ask_book, key=lambda o: (o.price, o.time))
        # You need to raise the following error if the side the order is for is ambiguous
        if order.side != OrderSide.BUY and order.side != OrderSide.SELL:
            raise UndefinedOrderSide("Undefined Order Side!")

    def amend_quantity(self, id, quantity):
        # Implement this function
        # Hint: Remember that there are two order books, one on the bid side and one on the ask side
        to_amend = None
        count = 0
        for o in self.bid_book:
            if o.id == id:
                to_amend = count
            count += 1
        if to_amend is not None:
            if self.bid_book[to_amend].quantity < quantity:
                raise NewQuantityNotSmaller("Amendment Must Reduce Quantity!")
            else:
                self.bid_book[to_amend].quantity = quantity
                return True
        to_amend = None
        count = 0
        for o in self.ask_book:
            if o.id == id:
                to_amend = count
            count += 1
        if to_amend is not None:
            if self.ask_book[to_amend].quantity < quantity:
                raise NewQuantityNotSmaller("Amendment Must Reduce Quantity!")
            else:
                self.ask_book[to_amend].quantity = quantity
                return True
        # You need to raise the following error if the user attempts to modify an order
        # with a quantity that's greater than given in the existing order
        # raise NewQuantityNotSmaller("Amendment Must Reduce Quantity!")
        return False

    def cancel_order(self, id):
        # Implement this function
        # Think about the changes you need to make in the order book based on the parameters given
        to_cancel = None
        count = 0
        for o in self.bid_book:
            if o.id == id:
                to_cancel = count
            count += 1
        if to_cancel is not None:
            del (self.bid_book[to_cancel])
            return True
        to_cancel = None
        count = 0
        for o in self.ask_book:
            if o.id == id:
                to_cancel = count
            count += 1
        if to_cancel is not None:
            del (self.ask_book[to_cancel])
            return True
        return False


# -----------------------------------------------------------

# Each trader can take a separate action chosen from the list below:

# Actions:
# 1 - Place New Order/Order Filled
# 2 - Amend Quantity Of An Existing Order
# 3 - Cancel An Existing Order
# 4 - Return Balance And Position

# request - (Action #, Trader ID, Additional Arguments)

# result - (Action #, Action Return)

# WE ASSUME 'AAPL' IS THE ONLY TRADED STOCK.
class ActionType(Enum):
    PLACE_ORDER = 1
    AMEND_ORDER = 2
    CANCEL_ORDER = 3
    RETURN_POSITION = 4


class Trader(MyThread):
    def __init__(self, id):
        super().__init__(id)
        self.book_position = 0
        self.balance_track = [1000000]
        self.order_on_book = False
        # the traders each start with a balance of 1,000,000 and nothing on the books
        # each trader is a thread

    def place_limit_order(self, quantity=None, price=None, side=None):
        # Make sure the limit order given has the parameters necessary to construct the order
        # It's your choice how to implement the orders that do not have enough information
        if quantity is not None and price is not None and side is not None:
            order = LimitOrder(self.id, 'AAPL', quantity, price, side, time.time())
            return (ActionType.PLACE_ORDER, self.id, order)
        else:
            raise Exception('Order does not have enough information!')
        # The 'order' returned must be of type LimitOrder

        # Make sure you modify the book position after the trade
        # You must return a tuple of the following:
        # (the action type enum, the id of the trader, and the order to be executed)

    def place_market_order(self, quantity=None, side=None):
        # Make sure the market order given has the parameters necessary to construct the order
        # It's your choice how to implement the orders that do not have enough information
        if quantity is not None and side is not None:
            order = MarketOrder(self.id, 'AAPL', quantity, side, time.time())
            return (ActionType.PLACE_ORDER, self.id, order)
        else:
            raise Exception('Order does not have enough information!')
        # The 'order' returned must be of type MarketOrder

        # Make sure you modify the book position after the trade
        # You must return a tuple of the following:
        # (the action type enum, the id of the trader, and the order to be executed)

    def place_ioc_order(self, quantity=None, price=None, side=None):
        # Make sure the ioc order given has the parameters necessary to construct the order
        # It's your choice how to implement the orders that do not have enough information
        if quantity is not None and price is not None and side is not None:
            order = IOCOrder(self.id, 'AAPL', quantity, price, side, time.time())
            return (ActionType.PLACE_ORDER, self.id, order)
        else:
            raise Exception('Order does not have enough information!')
        # The 'order' returned must be of type IOCOrder

        # Make sure you modify the book position after the trade
        # You must return a tuple of the following:
        # (the action type enum, the id of the trader, and the order to be executed)

    def amend_quantity(self, quantity=None):
        # It's your choice how to implement the 'Amend' action where quantity is not given
        if quantity is not None:
            return (ActionType.AMEND_ORDER, self.id, quantity)
        else:
            raise Exception('Quantity is not given!')
        # You must return a tuple of the following:
        # (the action type enum, the id of the trader, and quantity to change the order by)

    def cancel_order(self):
        # You must return a tuple of the following:
        # (the action type enum, the id of the trader)
        return (ActionType.CANCEL_ORDER, self.id)

    def balance_and_position(self):
        # You must return a tuple of the following:
        # (the action type enum, the id of the trader)
        return (ActionType.RETURN_POSITION, self.id)

    def process_response(self, response):
        # Implement this function
        # You need to process each order according to the type (by enum) given by the 'response' variable
        actiontype = response[0]
        if type(actiontype) == ActionType:
            if response[0] == ActionType.AMEND_ORDER:
                pass
            elif response[0] == ActionType.CANCEL_ORDER:
                self.order_on_book = False
            elif response[0] == ActionType.RETURN_POSITION:
                pass
            else:
                raise UndefinedResponse("Undefined Response Received!")
        elif type(actiontype) == int:
            if response[1][0] == ActionType.PLACE_ORDER:
                self.order_on_book = False
                if response[1][1].side == OrderSide.BUY:
                    self.book_position += response[1][1].quantity
                    self.balance_track.append(self.balance_track[-1] - response[1][1].quantity * response[1][1].price)
                else:
                    self.book_position -= response[1][1].quantity
                    self.balance_track.append(self.balance_track[-1] + response[1][1].quantity * response[1][1].price)
            else:
                raise UndefinedResponse("Undefined Response Received!")
        # If the action taken by the trader is ambiguous you need to raise the following error
        else:
            raise UndefinedResponse("Undefined Response Received!")

    def random_action(self):
        # Implement this function
        # According to the status of whether you have a position on the book and the action chosen
        # the trader needs to be able to take a separate action
        if not self.order_on_book:
            x = random.randrange(1, 4)
            order_type = OrderType(x)
            y = random.randrange(1, 3)
            order_side = OrderSide(y)
            price = random.randrange(90, 110)
            quantity = random.randrange(10000, 15000)
            if order_type == OrderType.LIMIT:
                action = self.place_limit_order(quantity, price, order_side)
                self.order_on_book = True
            elif order_type == OrderType.MARKET:
                action = self.place_market_order(quantity, order_side)
            else:
                action = self.place_ioc_order(quantity, price, order_side)
        else:
            z = random.randrange(1, 4)
            if z == 1:
                quantity = random.randrange(10000, 15000)
                action = self.amend_quantity(quantity)
            elif z == 2:
                action = self.cancel_order()
                self.order_on_book = False
            else:
                action = self.balance_and_position()
        return action
        # The action taken can be random or deterministic, your choice

    def run_infinite_loop(self):
        # The trader needs to continue to take actions until the book balance falls to 0
        # While the trader can take actions, it chooses from a random_action and uploads the action
        # to the exchange
        if self.balance_track[-1] < 0:
            #self.is_started = False
            return
        else:
            action = self.random_action()
            if action:
                trader_to_exchange.appendleft(action)
        # The trader then takes any received responses from the exchange and processes it
        #while True:
            if len(exchange_to_trader[self.id]) > 0 :
                response = exchange_to_trader[self.id].pop()
                self.process_response(response)


class Exchange(MyThread):
    def __init__(self):
        super().__init__()
        self.balance = [1000000 for _ in range(100)]
        self.position = [0 for _ in range(100)]
        self.matching_engine = MatchingEngine()
        # The exchange keeps track of the traders' balances
        # The exchange uses the matching engine you built previously

    def place_new_order(self, order):
        # The exchange must use the matching engine to handle orders given
        results = []
        # The list of results is expected to contain a tuple of the follow form:
        # (Trader id that processed the order, (action type enum, order))
        filled_orders = self.matching_engine.handle_order(order)
        if len(filled_orders) != 0:
            q = 0
            b = 0
            if order.side == OrderSide.BUY:
                for o in filled_orders:
                    if o.side == OrderSide.SELL:
                        self.position[o.id] -= o.quantity
                        self.balance[o.id] += o.quantity * o.price
                        results.append((o.id, (ActionType.PLACE_ORDER, o)))
                        q += o.quantity
                        b += o.quantity*o.price
                self.position[order.id] += q
                self.balance[order.id] -= b
                o = LimitOrder(order.id,order.symbol,q,b/q,order.side,order.time)
                results.append((o.id,(ActionType.PLACE_ORDER,o)))
            else:
                for o in filled_orders:
                    if o.side == OrderSide.BUY:
                        self.position[o.id] += o.quantity
                        self.balance[o.id] -= o.quantity * o.price
                        results.append((o.id, (ActionType.PLACE_ORDER, o)))
                        q += o.quantity
                        b += o.quantity * o.price
                self.position[order.id] -= q
                self.balance[order.id] += b
                o = LimitOrder(order.id, order.symbol, q, b / q, order.side, order.time)
                results.append((o.id, (ActionType.PLACE_ORDER, o)))
        # The exchange must update the balance of positions of each trader involved in the trade (if any)
        return results

    def amend_quantity(self, id, quantity):
        # The matching engine must be able to process the 'amend' action based on the given parameters
        try:
            true_or_false = self.matching_engine.amend_quantity(id, quantity)
        except NewQuantityNotSmaller:
            return None
        # Keep in mind of any exceptions that may be thrown by the matching engine while handling orders
        # The return must be in the form (action type enum, logical based on if order processed)
        return ActionType.AMEND_ORDER, true_or_false

    def cancel_order(self, id):
        # The matching engine must be able to process the 'cancel' action based on the given parameters
        try:
            true_or_false = self.matching_engine.cancel_order(id)
        except:
            return None
        # Keep in mind of any exceptions that may be thrown by the matching engine while handling orders
        # The return must be in the form (action type enum, logical based on if order processed)
        return ActionType.CANCEL_ORDER, true_or_false

    def balance_and_position(self, id):
        # The matching engine must be able to process the 'balance' action based on the given parameters
        return ActionType.RETURN_POSITION, (self.balance[id], self.position[id])
        # The return must be in the form (action type enum, (trader balance, trader positions))

    def handle_request(self, request):
        # The exchange must be able to process different types of requests based on the action
        # type given using the functions implemented above
        actiontype = request[0]
        if actiontype == ActionType.PLACE_ORDER:
            trader_id = request[1]
            trader_id_ob = []
            for o in self.matching_engine.ask_book:
                trader_id_ob.append(o.id)
            for o in self.matching_engine.bid_book:
                trader_id_ob.append(o.id)
            if trader_id in trader_id_ob:
                return None
            else:
                results = self.place_new_order(request[2])
        elif actiontype == ActionType.AMEND_ORDER:
            results = self.amend_quantity(request[1], request[2])
        elif actiontype == ActionType.CANCEL_ORDER:
            results = self.cancel_order(request[1])
        elif actiontype == ActionType.RETURN_POSITION:
            results = self.balance_and_position(request[1])
        else:
            # You must raise the following exception if the action given is ambiguous
            raise UndefinedTraderAction("Undefined Trader Action!")
        return results

    def run_infinite_loop(self):
        # The exchange must continue handling orders as orders are issued by the traders
        # A way to do this is check if there are any orders waiting to be processed in the deque
        if all(i <= 0 for i in self.balance):
            #self.is_started = False
            return
        while len(trader_to_exchange):
            request = trader_to_exchange.pop()
            return_function = self.handle_request(request)
            if return_function:
                if type(return_function) == list:
                    for action in return_function:
                        exchange_to_trader[request[1]].appendleft(action)
                else:
                    exchange_to_trader[request[1]].appendleft(return_function)
        # If there are, handle the request using the functions built above and using the
        # corresponding trader's deque, return an acknowledgement based on the response


if __name__ == "__main__":

    trader = [Trader(i) for i in range(100)]
    exchange = Exchange()

    exchange.start()
    for t in trader:
        t.start()

    exchange.join()
    for t in trader:
        t.join()

    sum_exch = 0
    for t in MyThread.list_of_threads:
        if t.id == "NoID":
            for b in t.balance:
                sum_exch += b

    print("Total Money Amount for All Traders before Trading Session: " + str(sum_exch))

    for i in range(10000):
        thread_active = False
        for t in MyThread.list_of_threads:
            if t.is_started:
                t.run_infinite_loop()
                thread_active = True
        if not thread_active:
            break

    sum_exch = 0
    for t in MyThread.list_of_threads:
        if t.id == "NoID":
            for b in t.balance:
                sum_exch += b

    print("Total Money Amount for All Traders after Trading Session: ", str(int(sum_exch)))