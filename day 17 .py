#creating class and object 
class Student:
    name="manvir"
s1=Student()
print(s1.name)
class Car:
    color="black"
    brand="mercedes"
car1=Car()
print(car1.color)

#init function 
class Student:
    def __init__ (self,fullname):
            print("my name is ..")
            self.name=fullname
naam=Student("manvir")
print(naam.name)

class Student:
    def __init__ (self,name,marks):#adding more than one paramter
        self.name=name
        self.marks=marks
s1=Student("manvir",99)
print(s1.name,s1.marks)

#problem set 

#problem 1 : first class 
class Car :
    def __init__(self,model,year,brand):
        self.model=model
        self.year=year
        self.brand=brand
car1=Car("bolero","2000","mahindra")
print(car1.model,car1.year,car1.brand)
car2=Car("alto","2005","marutu suzuki")
print(car2.model,car2.year,car2.brand)

#problem 2 :
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter (self):
        return 2*(self.length+self.width)
rect1=Rectangle(25,52)
print("area",rect1.area())
print("perimeter",rect1.perimeter())

#problem 3 :
class Student:
    school_name='dav'
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
stu1=Student("rahul",24)
stu2=Student("manvir",131)
print(Student.school_name,stu1.name,stu1.rollno)
print(Student.school_name,stu2.name,stu2.rollno)

#problem 4 : bankaccount class
class Bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"after deposit:{self.balance}")
    def withdrawel (self,amount):
        if amount>self.balance:
            print("invalid balance")
        else:
            self.balance-=amount
            print("after withdrawel the balance is :",self.balance)
    def show_balance(self):
        print("balance",self.balance)
account=Bankaccount("manvir",1000)
account.show_balance()
account.deposit(1500)
account.withdrawel(2000)

#problem 5 : student with grade 
class Student:
    def __init__(self,name,marks1,m2,m3):
        self.name=name
        self.marks1=marks1
        self.m2=m2
        self.m3=m3
    def average(self):
        return (self.marks1+self.m2+self.m3)/3
    def grade(self):
        avg=self.average()
        if avg>=90:
            return "a"
        elif avg>=80:
            return "b"
        elif avg>=70:
            return"c"
        elif avg >=60:
            return"d"
        else:
            return"f"
    def display(self):
        avg=self.average()
        g=self.grade()
        result="pass" if g != "f" else "fail"
        
        print("name",self.name)
        print("avg",round(avg,1))
        print("grade",g)
        print(result)
s=Student("manvir",58,99,99)
s.display()