languages = {"html","css","js","bootstrap"}

# counter =1
# for language in languages:
#     print(str(counter) +" : "+language)
#     counter+=1
i =1
json = {"name": "Coder Shiyar" , "age" : 21 ,"country":"Netherlands" }
for data in json :
    if data == "age": 
        break
    print(str(i) +" : "+ str(json[data]))
    i+=1
else:
    print("اكتمل من عرض بيانات ضمن فور لوب")