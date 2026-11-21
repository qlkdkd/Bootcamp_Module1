import json

with open('./json/myinfo.json') as f:
    data = json.load(f)

print(type(data))
print(data)