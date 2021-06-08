
# def printMessage(name,message):
#     print("Hi " + name + " " + message)

# printMessage("Coder Shiyar","welcome to python course")

# def printMessage(**langauges):
#     for lang in langauges:
#         print(langauges[lang] );
   
# printMessage(name1= "html",name2="css")    

def printMessage(*langauges):
    count = 1
    for lang in langauges:
        print(str(count) + " " + lang);
        count += 1
printMessage("html","css","javascript")    