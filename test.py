#!/usr/bin/env python3
import json

ex = {'key' : 7}
ex2 = {}
ex2['bigkey'] = ex

with open ('test.json', 'w') as fp:
    json.dump(ex2, fp)
