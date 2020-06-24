import requests
from utils import getpathfile
from properties import entrypoint


def getfiles():
    for i in entrypoint:
        r = requests.get(entrypoint[i])
        if r:
            with open(f'{getpathfile()}{i}.csv', 'wb') as f:
                f.write(r.content)
                print(f'Arquivo {i}.csv salvo com sucesso \n')
        else:
            print(f'Não foi possível fazer o download do arquivo {i}')

