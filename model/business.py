from utils import csvtodf
from model import schema


class Customer:
    def __init__(self):
        self._customer = csvtodf('customer', schema.customer)

    @property
    def getcustomer(self):
        return self._customer


class Geolocation:
    def __init__(self):
        self._geolocation = csvtodf('geolocation', schema.geolocation)

    @property
    def getgeolocation(self):
        return self._geolocation


class Items:
    def __init__(self):
        self._iems = csvtodf('items', schema.items)

    @property
    def getitems(self):
        return self._iems


class Orders:
    def __init__(self):
        self._orders = csvtodf('orders', schema.orders)

    @property
    def getorders(self):
        return self._orders


class Payments:
    def __init__(self):
        self._payments = csvtodf('payments', schema.payments)

    @property
    def getpayments(self):
        return self._payments


class Products:
    def __init__(self):
        self._products = csvtodf('products', schema.products)

    @property
    def getproducts(self):
        return self._products


class Reviews:
    def __init__(self):
        self._reviews = csvtodf('reviews', schema.reviews)

    @property
    def getreviews(self):
        return self._reviews


class Sellers:
    def __init__(self):
        self._sellers = csvtodf('sellers', schema.sellers)

    @property
    def getsellers(self):
        return self._sellers


