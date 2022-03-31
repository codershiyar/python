# String format() & f""     -     شرح طريقة تعامل مع نصوص بشكل افضل
# --------------------------------------------------------------------
name= "Coder Shiyar"
job="Software Engineer"
salary= 3000
# text="Good morning {0}. {0} is {1}. His salary is {2:.2f}".format(name,job,salary+(salary*0.10))
# print(text)
text2=f"Good morning {name}. {name} is {job}. His salary is {salary+(salary*0.10):.2f}"
print(text2)