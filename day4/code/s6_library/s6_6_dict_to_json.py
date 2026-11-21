import json

d = {'name':'hong',
     'birth':'0525'}

json_data = json.dumps(d)
print(json_data)
print(type(json_data))
