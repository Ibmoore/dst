#FUNCTIONS AND (CLASSES AND METHODS)
#ARGUMENTS: POsitional arg and Named arg
#String Formatting

def cities(count):
    print("There are", count, "cities on the map")

    cities(23)

    # def profile(1)
    #from multi import echo
    #return
num=30
for i in range(1, 31):
    print(i)



    #CLASSES
# class Notebook():
#     def__init__(self):
#         print("Home")
# Notebook()


# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(mysillyobject):
#     print("Hello my name is " + mysillyobject.name + " " + "I am 36")

# p1 = Person("John", 36)
# p1.myfunc()



class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()