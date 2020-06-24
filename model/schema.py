"""This file contains DF schemas in order to describe the structure of collected data"""

from pyspark.sql.types import *


customer = StructType([
    StructField("customer_id", StringType(), False),
    StructField("customer_unique_id", StringType(), False),
    StructField("customer_zip_code_prefix", IntegerType(), False),
    StructField("customer_city", StringType(), False),
    StructField("customer_state", StringType(), False)
])

geolocation = StructType([
    StructField("geolocation_zip_code_prefix", IntegerType(), False),
    StructField("geolocation_lat", FloatType(), False),
    StructField("geolocation_lng", FloatType(), False),
    StructField("geolocation_city", StringType(), False),
    StructField("geolocation_state", StringType(), False)
])

items = StructType([
    StructField("order_id", StringType(), False),
    StructField("order_item_id", StringType(), False),
    StructField("product_id", StringType(), False),
    StructField("seller_id", StringType(), False),
    StructField("shipping_limit_date", DateType(), False),
    StructField("price", FloatType(), False),
    StructField("freight_value", FloatType(), False)
])

orders = StructType([
    StructField("order_id", StringType(), False),
    StructField("customer_id", StringType(), False),
    StructField("order_status", StringType(), False),
    StructField("order_purchase_date", DateType(), False),
    StructField("order_approved_at", TimestampType(), False),
    StructField("order_delivered_carrier_date", DateType(), False),
    StructField("order_delivered_customer_date", DateType(), False),
    StructField("order_estimated_delivery_date", DateType(), False)
])

payments = StructType([
    StructField("order_id", StringType(), False),
    StructField("payment_sequential", IntegerType(), False),
    StructField("payment_type", StringType(), False),
    StructField("payment_installments", IntegerType(), False),
    StructField("payment_value", FloatType(), False)
])

products = StructType([
    StructField("product_id", StringType(), False),
    StructField("product_category_name", StringType(), False),
    StructField("product_name_lenght", IntegerType(), False),
    StructField("product_description_lenght", IntegerType(), False),
    StructField("product_photos_qty", IntegerType(), False),
    StructField("product_weight_g", IntegerType(), False),
    StructField("product_length_cm", IntegerType(), False),
    StructField("product_height_cm", IntegerType(), False),
    StructField("product_width_cm", IntegerType(), False)
])

reviews = StructType([
    StructField("review_id", StringType(), False),
    StructField("order_id", StringType(), False),
    StructField("review_score", IntegerType(), False),
    StructField("review_comment_title", StringType(), True),
    StructField("review_comment_message", StringType(), True),
    StructField("review_creation_date", TimestampType(), True),
    StructField("review_answer_timestamp", TimestampType(), True)
])

sellers = StructType([
    StructField("seller_id", StringType(), False),
    StructField("seller_zip_code_prefix", IntegerType(), False),
    StructField("seller_city", StringType(), False),
    StructField("seller_state", StringType(), False)
])