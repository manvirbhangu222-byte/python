a=input("enter the number ")
print(f"multiplication table of {a}is :")
try:
    for i in range(1,11):
        print(f"{int (a)} x {i}= {int(a)*i}")
except:
    print("invalid input ")
try:
    num=int(input("what is your number :"))
    a=[5,6]
    print(a[num])
except ValueError:
    print("input is wrong ")
except IndexError:
    print("index is wrong : ")
    
    #else block
try:
    num=int(input("what is your number "))
    a=[5,6,7]
   
except:
    print("input is wrong ")
else:
    print(a[num])

#finally 
try :
    num=int(input("what is ur number "))
    a=[3,4,5,6,7]
except ValueError:
    print("number is wrong ")
else:
    print(a[num])
finally:
    print("done!")
        
#problem set 
#problem 1 
a=int(input("enter first number "))
b=int(input("enter second number"))
try:
    divide=a/b
    print(divide)
except ZeroDivisionError :
    if b ==0:
        print("number is wrong ")

#problem 2 safe integer input 
while True:
    try:
        num=int(input("enter num: "))
        print(num)
        break
    except ValueError:
        print("error occured,try again  ")

#problem 3 : file safe reader 
f=input("enter file name : ")
try:
    file=open(f,'r')
    print(file.read())
except  FileNotFoundError :
    print("file not found,enter valid filename")
except PermissionError:
    print("permission denied")
finally:
    print("done")

#problem 4 : full error calculator :
try:
    num1=int(input("enter ur number "))
    op=input("select operator among +,-,*,/")
    num2=int(input('what is ur second number'))
    if op=="+":
        result=num1+num2
    elif op=="*":
        result=num1&num2
    elif op=="/":
        result=num1/num2
    elif op=="-":
        result=num1-num2
    else:
        print("enter valid operator")
    print("result:", result)
except ValueError as e:
    print("error",e)
except ZeroDivisionError as e :
    print("error,",e)            
        
#problem 5 :custom exception 
class InvalidAgeError(Exception):
    pass
def set_age(age):
    if age<0:
        raise InvalidAgeError("age cannot be less than zero ")
    elif age>150:
        raise InvalidAgeError("invalid age")
    else:
        print("age")
try:
    age=int(input("enter age "))
    set_age(age)
except InvalidAgeError as e:
    print("invalid",e)
except ValueError :
    print("enter valid ")
    
   
     

    
