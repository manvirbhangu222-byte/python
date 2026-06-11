tup=(1,2,3,True)
print(tup)
print(type(tup))

#for one value add coma at last 
tiple=(9,)
print(tiple)

#can also add string 
tupple=(1,2,3,4,'tupple')
print(tupple)

 #print single item in tuple
print(tup[0])
print(tup[1])
print(tup[2])
print(len(tup)) # length find

#if condition 
if 3 in tup:
    print("yes")

#operations in a tuple 
tup=(1,2,3,4,5,"manvir",)
list=list(tup)
list.append('singh')
list.pop(3)
list[2]=4
tup=tuple(list)
print(tup)

#concatenate two tupple 
tup1=(1,2,3,4,5,)
tup2=(6,7)
tup3=tup1+tup2
print(tup3)
# methods 
tup=(1,2,3,3,3,3)
res=tup.count(3)#count times 3 occurs
print("the number occurs:",res,"times")

result=tup.index(2)#tells  index of number first occurs
             #or 
result=tup.index(3,2,5)
print(result)

              # sets
s={1,2,2,2,3,34,}
print(s)
harry={None}
print(type(harry))
# set methods 
s1={1,2,3,4,5}
s2={6,1,2,3,4,7,} # union to join two sets 
print(s1.union(s2))
#update set
s1.update(s2)
print(s1)
#symmetric diference
s3=s2.symmetric_difference(s1)
print(s3)
#to add
s1.add(10)
print(s1)
#update
s1.update(s2)
print(s1)
#discard
s1.discard(5)
print(s1)
       



            #PROBLEM SETS 
# problem 1 tuple basics
tuple=("amritsar","bathinda","jalandhar","sangrur","gurdaspur")
print(tuple[0])
print(tuple[-1])

print("total count is :",len(tuple))

#problem2 :remove duplicates
n=[1,2,2,3,3,3,4,5,5,2,]
set=set(n)
print(set)

#problem 3 : set operations
a={1,2,3,4,5}
b={4,5,6,7,8}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#problem 4 : common elements
x=list(input("enter ur list", ).split(","))
y=list(input('enter your number ').split(','))
s1=set(x)
s2=set(y)
s3=s1.intersection(s2)
s3=list(s3)
print(s3)

#problem 5 : unique words
sentence=input("what's your sentence").split()
set=set(sentence)

print(len(set))

#problem 6 : symmetric difference
list1=[1,2,3,4,5,6]
list2=[1,5,6,7,8,3]
result=[]
for i in list1 :
    if i not in list2:
        result.append(i)
for i in list2:
    if i not in list1:
        result.append(i)
print(result)