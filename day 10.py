def calculategmean (a,b):
    mean =(a*b)/(a+b)
    print(mean)
def sizecheck (a,b):# defin ing one more function 
    if a > b:
        print("first is greater")
    else:
        print('second is greater or are equal')
def islssee (a,b):
    pass # to pass the function until   will later define it 
a=3
b=5
calculategmean(a,b)
sizecheck(a,b)
c=5
d=12
calculategmean(c,d)
sizecheck(c,d)
# arguments 
def average (a=3,b=9):# default args
    print("average is :," , (a+b)/2)
average()

average(b=4,a=3)#keyword argument we can interchange 
def average(*numbers):# variable length argument
    sum=0
    for i in numbers :
        sum=sum+i
    print("average is :",sum/len(numbers))
average(1,2,3,4)

# return 
def average(*numbers):# variable length argument
    sum=0
    for i in numbers :
        sum=sum+i
    return sum/len(numbers)
c=average(5,6,7,8,)
print(c)


          #problem statement
# problem 1 : basic function
def greet(name):
   
    for i in range (3):
        
        print("hello :",name)
name=input("enter your name : ")
greet(name)

# problrm 2 ; return value
def area_rectangle(length,width):
    return length*width
   
c=area_rectangle(12,34)
print(c)

# problem 3 : 
def greet(name,language='english'):
    if language=='hindi':
        print("namaste")
    else:
        print("hello")
greet('manvir','hindi')

# problem 4 : check palindrome 
def is_palindrome(word):
    if word==word[::-1]:# use in slicing the will print from last index to first index 
        return True
    else:
        return False
print(is_palindrome("madam"))

#problem 5 
def total (*args):
    sum=0
    average=0
    for i in args:
        sum=sum+i
        average=sum/len(args)
        return sum,average
c=total(1,2,3,3,3,3)
print("the sum and average are", c)

# problem 6 
 
def min_max(numbers):
    
  
     return min(numbers),max(numbers)
c=min_max([1,3,4,5,5,66])
print(c)

#problem 7 : fibonacci recursive 
def  fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
for i in range(10):
    print(fibonacci(i),end=' ')


        

    
