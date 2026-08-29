from enum import Enum

class Type(Enum):
    STOCK
    BOND
    OPTION

class Option_type(Enum):
    CALL
    PUT
    EXOTIC

class Origin(Enum):
    US
    EU

class Exotic_type(Enum):
    ASIAN
    BARRIER
    BINARY
    LOOKBACK
    BERMUDAN

class Stock:
    def __init__(self, price: int, devidend: float, type: Type, shares: int):
        self.price = price
        self.devidend = devidend
        self.type = STOCK
        self.shares = shares

    def dividend_yield(self):
        total_div = self.shares * self.devidend
        div_yield = (self.devidend / self.price) * 100
        return total_div, div_yield

class Bond:
    def __init__(self, price: int, coupon: float, type: Type, total: int):
        self.price = price
        self.coupon = coupon
        self.type = BOND
        self.total = total

    def coupon_yield(self):
        total_coup = self.total * self.coupon
        coup_yield = (self.coupon / self.price) * 100
        return total_coup, coup_yield

class Option:
    def __init__(self, price: int, type: Type, origin: Origin):
        self.price = price
        self.type = type
        self.origin = origin
