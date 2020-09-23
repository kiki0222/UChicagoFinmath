import time

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


from abc import ABC


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
            self.handle_limit_order(order)
        elif order.type == OrderType.MARKET:
            self.handle_market_order(order)
        elif order.type == OrderType.IOC:
            self.handle_ioc_order(order)
        else:
            # You need to raise the following error if the type of order is ambiguous
            raise UndefinedOrderType("Undefined Order Type!")

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
                    filled_id = []
                    q = order.quantity
                    for o in ask_order:
                        if o.price > order.price:
                            break
                        else:

                            if q < o.quantity:
                                filled_orders.append(order)
                                filled_orders.append(LimitOrder(o.id, o.symbol, q, o.price, \
                                                                o.side, o.time))
                                self.amend_quantity(o.id, o.quantity - q)
                                break
                            else:
                                filled_orders.append(o)
                                filled_id.append(o.id)
                                q = q - o.quantity
                    if q > 0:
                        self.insert_limit_order(order)
                        self.amend_quantity(order.id, q)
                    for idx in filled_id:
                        self.cancel_order(idx)
        elif side == OrderSide.SELL:
            bid_order = [o for o in self.bid_book if o.symbol == symbol]
            if len(bid_order) == 0:
                self.insert_limit_order(order)
            else:
                if bid_order[0].price < order.price:
                    self.insert_limit_order(order)
                else:
                    q = order.quantity
                    filled_id = []
                    for o in bid_order:
                        if o.price < order.price:
                            break
                        else:

                            if q < o.quantity:
                                filled_orders.append(order)
                                filled_orders.append(LimitOrder(o.id, o.symbol, q, o.price, \
                                                                o.side, o.time))
                                self.amend_quantity(o.id, o.quantity - q)
                                break
                            else:
                                filled_orders.append(o)
                                filled_id.append(o.id)
                                q = q - o.quantity
                    if q > 0:
                        self.insert_limit_order(order)
                        self.amend_quantity(order.id, q)
                    for idx in filled_id:
                        self.cancel_order(idx)
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
                ask_order_market = [o for o in ask_order if o.price == price]
                q = order.quantity
                filled_id = []
                for o in ask_order_market:
                    if q < o.quantity:
                        filled_orders.append(LimitOrder(order, id, order.symbol, order.quantity, \
                                                        price, order.side, order.time))
                        filled_orders.append(LimitOrder(o.id, o.symbol, q, o.price, o.side, o.time))
                        self.amend_quantity(o.id, o.quantity - q)
                        break
                    else:
                        filled_orders.append(o)
                        filled_id.append(o.id)
                        q = q - o.quantity
                for idx in filled_id:
                    self.cancel_order(idx)
        elif side == OrderSide.SELL:
            bid_order = [o for o in self.bid_book if o.symbol == symbol]
            if len(bid_order) > 0:
                price = bid_order[0].price
                bid_order_market = [o for o in bid_order if o.price == price]
                q = order.quantity
                filled_id = []
                for o in bid_order_market:
                    if q < o.quantity:
                        filled_orders.append(LimitOrder(order, id, order.symbol, order.quantity, \
                                                        price, order.side, order.time))
                        filled_orders.append(LimitOrder(o.id, o.symbol, q, o.price, o.side, o.time))
                        self.amend_quantity(o.id, o.quantity - q)
                        break
                    else:
                        filled_orders.append(o)
                        filled_id.append(o.id)
                        q = q - o.quantity
                for idx in filled_id:
                    self.cancel_order(idx)
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
                if ask_order[0].price < order.price:
                    for o in ask_order:
                        if o.price > order.price:
                            break
                        else:
                            q = order.quantity
                            if q < o.quantity:
                                filled_orders.append(order)
                                self.amend_quantity(o.id, o.quantity - q)
                                break
                            else:
                                filled_orders.append(o)
                                q = q - o.quantity
        elif side == OrderSide.SELL:
            bid_order = [o for o in self.bid_book if o.symbol == symbol]
            if len(bid_order) > 0:
                if bid_order[0].price > order.price:
                    for o in bid_order:
                        if o.price < order.price:
                            break
                        else:
                            q = order.quantity
                            if q < o.quantity:
                                filled_orders.append(order)
                                self.amend_quantity(o.id, o.quantity - q)
                                break
                            else:
                                filled_orders.append(o)
                                q = q - o.quantity
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
                self.bid_book[to_amend].quantity = quantity
        # You need to raise the following error if the user attempts to modify an order
        # with a quantity that's greater than given in the existing order
        # raise NewQuantityNotSmaller("Amendment Must Reduce Quantity!")
        # return False

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
        to_cancel = None
        count = 0
        for o in self.ask_book:
            if o.id == id:
                to_cancel = count
            count += 1
        if to_cancel is not None:
            del (self.ask_book[to_cancel])


matching_engine = MatchingEngine()
order_1 = LimitOrder(1, "S", 6, 10, OrderSide.BUY, time.time())
order_2 = LimitOrder(2, "S", 5, 10, OrderSide.BUY, time.time())
matching_engine.handle_limit_order(order_1)
matching_engine.handle_limit_order(order_2)

order = MarketOrder(5, "S", 5, OrderSide.SELL, time.time())
filled_orders = matching_engine.handle_market_order(order)
print(matching_engine.bid_book[0].quantity==1)
print(filled_orders[0].price==10)
