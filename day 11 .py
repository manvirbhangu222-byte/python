#string
name="manvir"
print(name[1]) # using index

# using len function
print(len(name))

#slicing to print more than one character
print(name[3:5])
print(name[1:])
print(name[::-1]) # reverses order 

#string methods 
a="!!!!!!harry1!!!!"
#upper case
print(a.upper())

#lower case
print(a.lower())

 #strip removes that character from whole string 
print(a.strip("!"))

# rstrip removes last character only 
print(a.rstrip("!"))

#replace
print(a.replace("harry","john"))

# split split into list
b="harrry is a good boy "
print(b.split(" "))

#capitalize capital first character and lower rest of them 
print(b.capitalize())

#centre 
print(b.center(50))

#count()
str="manvir singh bhangu"
print(str.count('a'))

#endswith()
print(str.endswith("hu"))

#find()
print(str.find("s"))

# index
print (str.index("s"))

#      problem set 
#  problem 1 : string transformations
string="my name is manvir"
print(string.upper())
print(string.title())
print(string.lower())
print(string[::-1])

# problem 2 : word counter
sentence=input("enter ur sentence ")
list=sentence.split()
print(len(list))

# problem 3 :
str=input("what is ur string : ")
result=""
for i in str[0:-1]:
    if i in "aeiou":
       result=result+"*"
    else:
        result=result+i
print(result)

#problem 4
email=input("what is ur email:")
str=(email.find("@"))
dot=(email.find("."))

if str ==-1 or dot==-1:
        print("error")
elif str==-0:
        print("error")
elif str>dot:
        print("error")
else:
        print(email)
       
#problem 5 
text=input("what is your string : ")
count={}
for ch in text:
    if ch!=" " :
        if ch in count:
            count[ch]+=1
        else:
            count[ch]=1
max_char=""
max_count=0
for ch in count:
    if count[ch]>max_count:
        max_count=count[ch]
        max_char=ch
print("most frequent ", max_char,"appears", max_count)

# problem 6 :title formatter
sentence = input()

lower_words = {'a', 'an', 'the', 'in', 'on'}

words = sentence.split()

result = []
for i, word in enumerate(words):
    if word.lower() in lower_words:
        result.append(word.lower())
    else:
        result.append(word.capitalize())

print(" ".join(result))

# problem 7 : caesar cipher
message = input()
shift = int(input())

encoded = ""

for ch in message:
    if 'a' <= ch <= 'z':
        new_char = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        encoded += new_char
    elif 'A' <= ch <= 'Z':
        new_char = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        encoded += new_char
    else:
        encoded += ch

print(encoded)
   
        
