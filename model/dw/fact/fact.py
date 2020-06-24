from business.business import Customer, Geolocation, Orders, Products, Reviews, Sellers, Items, Payments
from utils import time_transformation, d_transformation, insert
from DAO.spark import log


class Fact:
    def __init__(self):
        log("Initalizing Fact objects")
        self.customers = Customer().getcustomer
        self.geolocation = Geolocation().getgeolocation
        self.items = Items().getitems
        self.orders = Orders().getorders
        self.payments = Payments().getpayments
        self.products = Products().getproducts
        self.reviews = Reviews().getreviews
        self.sellers = Sellers().getsellers

        log("Initializing Data Transformation and Ingestion Process")

        self.df = self.prepair()
        self.middle = self.arrange()
        self.middle = self.transformation()
        self.fact = self.finall()

        insert(self.fact, "fact_orders")

    def prepair(self):
        return self.customers.join(self.orders, on="customer_id", how="inner").join(self.payments, on="order_id", how="inner")\
            .join(self.items, on="order_id", how="inner").join(self.reviews, on="order_id")

    def arrange(self):
        return self.df.join(self.sellers, on="seller_id", how="inner")

    def finall(self):
        return self.middle.select(
            self.middle['order_id'], self.middle['customer_id'], self.middle['order_item_id'],
            self.middle['customer_zip_code_prefix'], self.middle['order_status'],
            self.middle['order_purchase_date'], self.middle['order_approved_at'],
            self.middle['order_delivered_carrier_date'], self.middle['order_delivered_customer_date'],
            self.middle['order_estimated_delivery_date'], self.middle['payment_type'], self.middle['payment_installments'],
            self.middle['payment_value'], self.middle['product_id'], self.middle['seller_id'], self.middle['seller_zip_code_prefix'],
            self.middle['shipping_limit_date'], self.middle['review_id']
        )

    def transformation(self):
        df = time_transformation(self.middle)
        return d_transformation(df)
Fact()