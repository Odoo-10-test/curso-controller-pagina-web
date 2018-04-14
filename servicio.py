# /usr/bin/env python
# coding: utf-8
import sys
from pprint import pprint

import requests

HOST = 'localhost'
PORT = '8069'
URI = 'web/clientes/json/'
URL = 'http://%s:%s/%s' % (HOST, PORT, URI)


def consumir(url, name):
    headers = {
        'Content-Type': 'application/json',
    }

    data = '{"params": {"name":"prakashsharma","email":"prakashsharmacs24@gmail.com","phone":"+917859884833"}}'
    print '\n\n\n%s\n\n\n' % url
    res = requests.post(url=url, headers=headers, data=data)
    pprint(res.json())


if __name__ == '__main__':
    NAME = raw_input('Indique el nombre del cliente: ')
    consumir(URL, NAME)
    sys.exit(0)
