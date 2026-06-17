                 #dictionaries
dict={'name':'manvir','rollno':2304131,'cgpa':8.6,'city':'amritsar'}
for key,value in dict.items():
    print(key,":",value)
#2
dict={'name':'manvir','rollno':2304131,'cgpa':8.6}
dict.update ({'branch':'cse','city':'amritsar'})
dict['name']='man'
print(dict)

#3
str=input("enter your word :")
dict={}
for i in str:
    dict[i]=dict.get(i,0)+1
print(dict)

#4
sentence=input("what's your sentence")
words=sentence.split()
dict={}
for i in words:
    dict[i]=dict.get(i,0)+1
print(dict)

#5
dict={'a':1, 'b':2, 'c':3}

new_dict={v: k for k, v in dict.items()}
         
print(new_dict)

#problem 6 
n=list(input("what are ur numbers :"))
count={}
for i in n :
    count[i]=count.get(i,0)+1
max=max(count,key=count.get)
print('most common :' ,max)

#problem 7
dict=[{'names':'manvir','marks_math':66,'marks_science':80},
      {'names':'singhh','marks_math':60,'marks_science':88},
      {'names':'bhangu','marks_math':6,'marks_science':8}]
top=""
highest=0
for i in dict:
   average=(i['marks_math']+i['marks_science'])/2
   if average > highest:
      highest=average
      top=i
    

print('top',top['names'],"with avg:",average)


                                   #problem set
#problem 1 
contact_book={}
i=0
while True:
    n=input("\n.............MENu.........")
    print("1.ADD")
    print("2.search")
    print("3.DELETE")
    print("4.SHOW ALL")
    print("5.EXIT")
    choice=int(input("select ur choice :"))
    if choice==1:
        
        name=input("enter ur name ")
        phone=input("enter ur phone")
        contact_book[name]=phone
        print(contact_book)
    elif choice ==2:
        name=input("enter the name to search :")
        if name not in contact_book:
            print("not find")
        else:
            print(contact_book[name],[])
    elif choice==3:
        name=input("enter the name to delete:")
        if name not in contact_book:
            print("name is not present : ")
        else:
         del contact_book[name]  
         print("contact deleted successfully")
    elif choice==4:
        if contact_book:
            print("\n all contacts ")
            for name,phone in contact_book.items():
                print(f"{name},{phone}")
        else:
            print("no contacts available")
    elif choice==5:
        print("exiting contact book....")
        break
    else:
        print("enter valid number between 1-5")


#problem 2 
students=[
    {"name":"manvur","marks":"86"}
    {"name":"amit","marks":"8"}
   { "name":"priya","marks":"96"}
   {"name":"neha","marks":"90"}
]
print("all students")
for student in students:
    print(["name"],"",student["marks"])

top_student=student[0]
for student in students :
    if student ["marks"]>top_student["marks"]:
        top_student=student 

total=0
for student in students :
    total=total+student["marks"]
average=total/len(students)

passed=0
for student in students:
    if student["marks"]>=40:
        passed+=1
print("\n top scorer ", top_student["name"],top_student["marks"])
print("average marks:",average)
print("passes student: ",passed)
