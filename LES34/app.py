import json
# json.dumps()        يمكنك استخدامها لتحويل بيانات من نوع اوبجكت ديكجوناري إلى بيانات بصيغة جي سون
# json.loads() يتم استخدامها لتحويل البيانات مكتوبة بصيغة جي سون إلى بيانات بصيغة اوبجكت ديكجوناري


data= '{"name": "Shiyar",  "age" : 21 ,  "isMaried" : false }'
data_dict = json.loads(data)
print(data_dict["name"]   )         
print( type(json.loads(data))  )  


# data= {
#      "name": "Shiyar",
#       "age" : 21 ,
#       "isMaried" : False
#     }

# print( json.dumps(data) )         
# print( type(json.dumps(data))  )  


# If you have a JSON string, you can parse it by using the json.loads() method.
# If you have a Python object, you can convert it into a JSON 
# string by using the json.dumps() method.


