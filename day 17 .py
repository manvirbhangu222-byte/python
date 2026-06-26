# #creating class and object 
# class Student:
#     name="manvir"
# s1=Student()
# print(s1.name)
# class Car:
#     color="black"
#     brand="mercedes"
# car1=Car()
# print(car1.color)

##init function 
# class Student:
#     def __init__ (self,fullname):
#             print("my name is ..")
#             self.name=fullname
# naam=Student("manvir")
# print(naam.name)

# class Student:
#     def __init__ (self,name,marks):#adding more than one paramter
#         self.name=name
#         self.marks=marks
# s1=Student("manvir",99)
# print(s1.name,s1.marks)

##problem set 

##problem 1 : first class 
class Car :
    def __init__(self,model,year,brand):
        self.model=model
        self.year=year
        self.brand=brand
car1=Car("bolero","2000","mahindra")
print(car1.model,car1.year,car1.brand)
car2=Car("alto","2005","marutu suzuki")
print(car2.model,car2.year,car2.brand)