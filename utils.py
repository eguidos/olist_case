from config.spark import Spark
import os
from pyspark.sql import functions as F


def getspark():
    sc = Spark()
    return sc.spark


def getpathfile():
    path = os.path.join(os.path.dirname(__file__), '../dataengineering/resources/files/')
    return path


def csvtodf(file, schema):
    return getspark().read \
        .option("multiline", "true") \
        .option("quote", '"') \
        .option("quote", ",") \
        .option("header", "true") \
        .option("escape", "\\") \
        .option("escape", '"') \
        .schema(schema) \
        .csv(getpathfile()+"/"+file+'.csv')



def insert(dataframe, table):
    dataframe.write.format('jdbc').options(url='jdbc:mysql://localhost/olist?autoReconnect=true&useSSL=false',
                                            driver='com.mysql.jdbc.Driver',
                                            dbtable=table,
                                            user='root',
                                            password='admin').mode('overwrite').save()
    return True


def date_transformation(df):
    return df.withColumn("order_purchase_date", F.date_format("order_purchase_date", "yyyy-MM-dd"))


def time_t(df):
    return df.withColumn("order_purchase_date", F.date_format("order_purchase_date", "HH:mm"))


def time_transformation(df):
    return df.withColumn("order_date", F.split(F.date_format("order_approved_at", "yyyy-MM-dd"), " ").getItem(0))


def d_transformation(df):
    return df.withColumn("order_purchase_date", F.split(F.date_format("order_purchase_date", "yyyy-MM-dd"), " ").getItem(0))


