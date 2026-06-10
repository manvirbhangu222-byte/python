# problem 1 
fruits=["mango","apple","banana","grapes","kiwi"]

print(fruits[0],fruits [4],fruits[2] ,sep ="\n")

#problem2 
numbers=[1,2,3,4,5]
total=0
maximum=numbers[0]
minimum=numbers[0]
for num in numbers:
    total=total+num
    if num>maximum:
        maximum=num
    if num<minimum:
        minimum=num
    average=total/len(numbers)
print(total,maximum,minimum)

# problem 3
names=["manvir","singh","bhangu"]
names.append("bhangwan")
names.append("jatt)")
names.remove("singh")
print("appended version=:",names)
print("removed version : ",names)

# problem 4
list=[1,2,3,4,5]
reverse=[]
for i in range(len(list)-1,-1,-1):
   reverse.append(list[i])
print(reverse)

#problem 5
list=[1,2,2,3,3,3,4]
for i in list:
    count=0
    for x in list:
        if x==i:
            count=count+1
    print (i ,"appears",count,"times")

#problem 6 
list=[1,5,4,3,2]

for i in range(len (list)):
    for j in range(len(list)-1-i):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
 

print(list)

# problem 7 
num=[]
for i in range(5):
    num.append(int(input("your numbe :")))
    max=num[0]
for j in num :
        if j>max:
            max=j
second=None
for j in num:
        if j!=max:
            if second is None or j>second:
                second=j
print("second largest number is : ", second)