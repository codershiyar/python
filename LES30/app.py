# try                      تتيح لك تجربة جزء من اكوادك الذي تختارها لتحقق أن كان هناك بها خطا او لا 
# except                 تتيح لك معالجة الخطأ في حال حدوثها مثل تنفيذ اوامر اخرى في حال حدث خطا ما
# finally             تتيح لك تنفيذ التعليمات البرمجية ، بغض النظر عن نتيجة المحاولة- تري و اكسبت
# else  يمكنك استخدامها لتنفيذ التعليمات البرمجية الذي تحدده ليتم تنفيذها في حالة عدم ظهور أخطاء


try:
    print(name)
except:
    print("لم يتمكن من ايجاد المتغير الذي قمنا بتحديده")
else:
    print("لم يتواجد اي اخطا")    
# finally: 
#     print("تم تنفيذ اوامر ضمن حقل finally")











# The try block lets you test a block of code for errors.
# --------------------------------------------------------------------------------------------------
# The except block lets you handle the error.
# --------------------------------------------------------------------------------------------------
# The finally block lets you execute code, regardless of the result of the try- and except blocks.
# --------------------------------------------------------------------------------------------------
# You can use the else keyword to define a block of code to be executed if no errors were raised:

