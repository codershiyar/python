import os
import shutil
# Python Delete File - شرح كيفية حذف الملفات بواسطة بايثون
# --------------------------------------------------------------------
# os    مكتبة التالية يتيح لنا امكانية لحذف الملفات بواسطة بايثون
# os.remove() To delete a file            يستخدم لحذف ملف الذي تحدده
# os.rmdir() To delete an empty folder   يستخدم لحذف مجلد الذي تحدده
# Note: You can only remove empty folders.
# --------------------------------------------------------------------
# shutil  يتيح لنا حذف مجلد كامل حتى ان كان المجلد المحدد غير خالي
#   shutil.rmtree('/folder_name', ignore_errors=True)

# if os.path.exists("app.html"):
#       os.remove("app.html")
#       print("تم حذف الملف بنجاح")
# else:
#       print("لم يتم ايجاد الملف المحدد")
# os.rmdir("files")
shutil.rmtree("files", ignore_errors=True)



















# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")

# import shutil 
#   shutil.rmtree('/folder_name', ignore_errors=True)
