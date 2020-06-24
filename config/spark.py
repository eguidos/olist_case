from pyspark.sql import SparkSession


class Spark:
    def __init__(self):
        self.spark = SparkSession.builder \
            .appName("data_import") \
            .config("spark.dynamicAllocation.enabled", "true") \
            .config("spark.shuffle.service.enabled", "true") \
            .enableHiveSupport() \
            .getOrCreate()

    def set(self):
        return self.spark


def log(text):
    log4jLogger = Spark().set()._jvm.org.apache.log4j
    log = log4jLogger.LogManager.getLogger(__name__)
    log.warn(text)


