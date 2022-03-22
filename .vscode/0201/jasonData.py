# coding:utf-8

import json

data = {
    'name': 'Jerry',
    'phone': '0912345678',
    'age': 18
}

jsonStr = json.dumps(data, sort_keys=False, indent=3)
print(jsonStr)  # JSON
# {
#    "age": 18,
#    "name": "Jerry",
#    "phone": "0912345678"
# }

newData = json.loads(jsonStr)   # Dictionary
print(newData)
# {'age': 18, 'name': 'Jerry', 'phone': '0912345678'}
