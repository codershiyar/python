class App:
    course = "Python"
    def getName():
        return "Coder Shiyar"

    def print_message():
        print("تم استدعاء الميتود")
    def calculator(number1 , number2):
        App.print_message()
        print("Course name : " + App.course)
        result = number1 + number2
        return result
        
print("Result of 20 + 10 = " + str(App.calculator(20,10)) )  




