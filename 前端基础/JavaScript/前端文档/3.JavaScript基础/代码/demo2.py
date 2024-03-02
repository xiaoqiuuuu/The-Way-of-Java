






dic =  {
    'name':"alvin",
    "age":18
}

import json

json_str = json.dumps(dic)
print(json_str)  # '{"name": "alvin", "age": 18}'

res = '{"state":true,"data":[123,234,345]}'

data = json.loads(res)
print(data,type(data))
print(data["state"])





