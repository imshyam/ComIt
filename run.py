import requests

# constants
RUN_URL = u'http://api.hackerearth.com/code/run/'

CLIENT_SECRET = '807834b1529d46b54b22f7427156bf95562db4df'

source = open('ex.c', 'r')
"""
test.py
#! -*- coding: utf-8 -*-

def square(no):
    return no * no

print(square(-23))
"""

data = {
    'client_secret': CLIENT_SECRET,
    'async': 0,
    'source': source.read(),
    'lang': "C",
    'time_limit': 5,
    'memory_limit': 262144,
}

r = requests.post(RUN_URL, data=data)
source.close()
payload= r.json()
run_status = payload.get('run_status')
o = run_status['output']
print o
