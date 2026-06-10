def main():
    x=int(input("what's x :"))
    if is_even(x):
        print("even")
    else :
        print("odd")
def is_even (n):
    if n%2==0:
        return True
    else:
      
      main()



#match keyword !
name=input("enter your name :")
match name:
    case "harry"|"hermoid"|"ron":
        print("grayffindor")
    case "draco":
        print("slytherin")
    case _:
        print ("who the fuck is this ?")



#PROBLEM SET -> !

#1
number=int(input("what's your number "))
if number>0:
    print("number is positive")
elif number<0:
    print("the number is negative")
else:
    print("the number isn zer")

#2
age=int(input("what's your age putt: "))
if age>=18:
    print("you are eligible")
else:
    print("you cannot vote")

#3
x=int(input("give value of x "))
y=int(input("give value of y "))
if x>y:
    print("x is larger")
elif y>x:
    print("y is larger")
else:
    print("both are equal")

#4
marks=int(input("give input between1-100 :"))
if marks>=90:
    print("GRADE A")
elif marks>=80:
    print("GRADE B")
elif marks>=70:
    print("GRADE C ")
elif marks >=60:
    print("GRADE D")
else :
    print("GRADE F")

#5
x=int(input("give first number "))
y=int(input("give second number "))
z=int(input("give third number "))
if y<x>z :
    print("x is largest")
elif x<y>z :
    print("y is largest")
else :
    print("z is the largest ")

#6
year=int(input("give the year "))
if (year%40==0 and year%100!=100)or year%400==0 :
    print("the given year is leap year")
else :
    print("the year is not the leap year")

# 6

username = input("give the username  ")
password=input("give the password ")

if username=="manvir" and password=="1234":
    print(" login successfully ")
else :
    print ("access denied chal fuddu dfa ho")

