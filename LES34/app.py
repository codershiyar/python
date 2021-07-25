import json
# json.dumps()        يمكنك استخدامها لتحويل بيانات من نوع اوبجكت ديكجوناري إلى بيانات بصيغة جي سون
# json.loads() يتم استخدامها لتحويل البيانات مكتوبة بصيغة جي سون إلى بيانات بصيغة اوبجكت ديكجوناري

data = {
        "name":"Shiyar",
        "age": 21 ,
         "isMarried":False
        }

data_json = '{"name": "Shiyar", "age": 21, "isMarried": false}'
data_json = json.loads(data_json) 
print(data_json["name"])
# print(type( json.loads(data_json)) )



# If you have a JSON string, you can parse it by using the json.loads() method.
# If you have a Python object, you can convert it into a JSON 
# string by using the json.dumps() method.


