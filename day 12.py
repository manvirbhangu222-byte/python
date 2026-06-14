num=[1,2,3,4,5,6,7,8,9,10]
my_list=[]
for i in  num:                       # traditional method 
    my_list.append(i)
print (my_list)\

# comprehension list 
my_list=[i for i in num]
print(my_list)

# i want 'n&*n for each n in nums 
my_list=[i*i for i in num]
print(my_list)

# using map + lambda 
my_list=list (map(lambda i:i*i,num))
print(my_list )

# i want 'n' for each 'n' in num if 'n' is even 
my_list=[n for n in num if n%2==0]
print(my_list)

# i want (letter,num) pair for each letter in "abcd' and each num in '0123"
my_list=[(letter,num) for letter in "abcd" for num in range (4)]
print (my_list)

#dictionay comprehension 
# zip function 
name=['bruce','clark','peter','logan','wade']
heros=['superman','siderman','batman','wolverine','deadpool']
print (list (zip(name,heros)))

# i want a dict {'namer': 'heros'} for each name , hero in zipp (name,hero )
my_dict={}
for name,hero in list(zip(name,heros)):      #traditional method 
    my_dict[name]=hero
print(my_dict)
#comprehension method 
my_dict={name:heros for name,heros in list(zip(name,heros))}
print(my_dict)

#set comprehension 
nums=[1,2,3,4,5,6,7,8,9,10]
my_set={n for n in nums}
print(my_set)

                              #PROBLEM SET 

# problem 1 : square list 
my_list=[i for i in range(1,16)]
print(my_list )

#  problem 2 : filter evens 
num=[1,2,3,4,5,6,7,8,9,10]
my_list=[n for n in num if n%2==0]
print(my_list )

#  problem3: uppercase names
names= ['raj', 'priya', 'amit']
my_list=[name.upper() for name  in names]
print(my_list)

# problem 4 : word length dict
words=['abc','def','ghi']
dict={word:len(word) for  word in words }
print(dict)

#problem 5 : remove short words
sentence=(input("what is your sentence : "))
my_list=[i for i in sentence.split() if len(i)>4]
print(my_list)


