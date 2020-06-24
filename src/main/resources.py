import requests
from utils import getpathfile
from properties import entrypoint


def getfiles():
    for i in entrypoint:
        r = requests.get(entrypoint[i])
        if r:
            file = getpathfile() + "/" + i + ".csv"
            with open(file, 'wb') as f:
                f.write(r.content)

