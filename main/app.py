from model.dw.dim.dimension import Dim
from model.dw.fact.fact import Fact
from config.spark import log

class Main:
    def __init__(self):
        Fact()
        Dim()


if __name__ == '__main__':
    log("Initizaling the process of collecting, transforming and inserting consolidate data into OLIST Database")
    Main()
    log("Execution has been finished")

