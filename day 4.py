i=3
while i<5:
    print("ki haal aa mitro " )
    i=i+1


# for loop 
for i in  [0,1,2]:
    print("meow")
        #  or
for i in range(7):
    print("meow")
while True:
    n=int(input("what's value of n ?"))
    if n>5:
      break
for i in range (n):
    print("meow")

         # list
students=["manvir","singh","bhangu"]
for students in students:
    print(students)
       
          #len
students=["manvir","singh","bhangu"]
for i in range(len(students)):
    print(i+1,students[i])

          #dict
students={"hermione" : "grayffindor" ,
            "harry"  : "graffindor" ,
            "ron" : "slytherin" }
for student in students:
    print(student , students[student])




             # PROBLEM SET 
#1 
for i in range(10):
    print(i=1, sep="\n")

#2
total=0
for i in range(1,101):
    total=total+i
print("sum=",total)

#3
number=int(input("what's your number"))
for multiply in range (1,11):
    print(f"{number} x {multiply} = " , multiply*number)

#4
for i in range (1,51):
    if i%2==1:
        continue
    print(i)

#5
number=int(input("what is your number "))
reversed=0
while number>0:
    digit=number%10
    reversed=reversed*10+digit
    number=number//10

    print("reversed: ",reversed)

#6
num=int(input(" give ur number : "))
result=1
for i in range(1,num+1):
    result*=i
    print(result)

#7
n=int(input("give ur number :"))
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
else :
        print("prime")

        