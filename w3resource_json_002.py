#convert Python object to JSON data
import json
#a Python object (dict):
python_obj = {
    "name": "David",
    "class": "I",
    "age": 6
}
print(type(python_obj))
# convert into JSON:
jdata = json.dumps(python_obj)

# result is JSON string:
print(jdata)