"""MYSql configurations"""

confi = {
  'user': 'root',
  'password': 'admin',
  'host': '127.0.0.1',
  'database': 'industry'
}

"""Entry Point for all CSV files"""

entrypoint = {
  'customer': 'https://raw.githubusercontent.com/olist/work-at-olist-data/master/datasets/olist_customers_dataset.csv',
  'geolocation': 'https://raw.githubusercontent.com/olist/work-at-olist-data/master/datasets/olist_geolocation_dataset.csv',
  'items': 'https://raw.githubusercontent.com/olist/work-at-olist-data/master/datasets/olist_order_items_dataset.csv',
  'payments': 'https://raw.githubusercontent.com/olist/work-at-olist-data/master/datasets/olist_order_payments_dataset.csv',
  'reviews': 'https://raw.githubusercontent.com/olist/work-at-olist-data/master/datasets/olist_order_reviews_dataset.csv',
  'orders': 'https://raw.githubusercontent.com/olist/work-at-olist-data/master/datasets/olist_orders_dataset.csv',
  'products': 'https://raw.githubusercontent.com/olist/work-at-olist-data/master/datasets/olist_products_dataset.csv',
  'sellers': 'https://raw.githubusercontent.com/olist/work-at-olist-data/master/datasets/olist_sellers_dataset.csv',
}