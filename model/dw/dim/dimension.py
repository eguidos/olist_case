from model.business import Customer, Geolocation, Orders, Products, Reviews, Sellers, Items
from utils import insert, date_transformation, time_t
from config.spark import log


class Dim:
    def __init__(self):
        log("Initalizing Dimension objects")
        self._customer = Customer().getcustomer
        self._geolocation = Geolocation().getgeolocation
        self._products = Products().getproducts
        self._reviews = Reviews().getreviews
        self._sellers = Sellers().getsellers
        self._items = Items().getitems
        self._orders = Orders().getorders

        log("Initializing Data Transformation and Ingestion Process")

        self.transform_customer()
        self.transform_location()
        self.transform_reviews()
        self.transform_sellers()
        self.transform_items()
        self.transform_date()
        self.transform_time()

    def transform_customer(self):
        insert(self._customer.select('customer_id', 'customer_unique_id'), "dim_customer")


    def transform_location(self):
        insert(self._geolocation.select("geolocation_zip_code_prefix", "geolocation_lat", "geolocation_lng",
                                               "geolocation_city", "geolocation_state").distinct(), "dim_location")

    def transform_reviews(self):
        insert(self._reviews.select("review_id", "review_score", "review_comment_title", "review_comment_message"), "dim_reviews")

    def transform_sellers(self):
        insert(self._sellers.select("seller_id"), "dim_sellers")

    def transform_items(self):
        insert(self._items.select("product_id", "price", "freight_value"), "dim_items")

    def dim_date(self):
        return self._orders.select("order_purchase_date")

    def transform_date(self):
        df = date_transformation(self.dim_date())
        insert(df.select('order_purchase_date').distinct(), "dim_date")

    def transform_time(self):
        df = time_t(self.dim_date())
        insert(df.select("order_purchase_date").distinct(), "dim_time")

