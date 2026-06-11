# # DICTIONARIES
# student={'name':'manvir','course':'btech cse','age':'21'}
# print(student['age'])
# print(student.get("phone",'nhi haiga '))

# #to add in dict
# student={'name':'manvir','course':'btech cse','age':'21'}
# student['phone']='420'
# print(student['phone'])

# #to update the value 
# student.update({'name':'manvir','age':'23'})
# print (student)

# #to remove key
# del student["name"]
# print(student)
#       # or pop method
# age=student.pop("age")
# print (student)
# print(age) # to get return value of popped item 

# print(len(student)) # to see number of keys 
# print(student.keys())# to see all keys
# print(student.values()) # to seee all values 
# print(student.items()) # to see both keys and values 
# # to print both values and keys we use .items
# for key,value in student.items():
#     print(key,value)
#     #simple loop 
# for k in student:# will print only the keys 
#     print(k)

                                    # problem set
# problem 1 : student dictionary 
#student={'name': 'Manvir singh','roll no' : 2304131,'cgpa': 8.5,'branch':'cse','city':'amritsar'}
# for key,value in student.items():
#     print(f"{key}:{value}")

# provlem 2 :update and add
# dict={'name':'manvir singh','age':21,'caste':'jatt mehkma' }
# dict.update({'name' : 'bhangu','address' : 'bhangwan','city':'amritsar'})
# del dict['caste']
# print('final dict:',dict)

# problem 3 : character count
# string=input("what's your string:")
# dict={}
# for char in string :
#     dict[char]=dict.get(char,0)+1

# print(dict)
    
#problem 4 :word frequency
# sentence=input("enter your sentence:")
# words=sentence.split()
# dict={}
# for i in words:
#     dict[i]=dict.get(i,0)+1
# print (dict)

#problem 5 
# dict={'a':1,'b':2,'c':3}
# new_dict={v:k for k,v in dict.items()}
# print(new_dict)

#problem 6 
# n=list(input("what are ur numbers :"))
# count={}
# for i in n :
#     count[i]=count.get(i,0)+1
# max=max(count,key=count.get)
# print('most common :' ,max)

#problem 7
# dict=[{'names':'manvir','marks_math':66,'marks_science':80},
#       {'names':'singhh','marks_math':60,'marks_science':88},
#       {'names':'bhangu','marks_math':6,'marks_science':8}]
# top=""
# highest=0
# for i in dict:
#    average=(i['marks_math']+i['marks_science'])/2
#    if average > highest:
#       highest=average
#       top=i
    

# print('top',top['names'],"with avg:",average)