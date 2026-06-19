f=open('myfile.txt','r')
text=f.read()
print(text)
f.close()

#write mode 
f=open('file','w')
f.write("hello world !!!!!!!!!!!!!!!")

#problem set 
#problem 1 
with open('info','w')as f :
    f.write(" name : manvir \n city: amritsar \n age 22")
    f.close()
f=open("info",'r')
print(f.read())

#sproblem 2 : append 
with open ('info.txt','w') as f :
    f.write('''name:manvir\nname:singh\nname:bhangu''')

with open('info.txt','a') as f :
  f.write("\nname:manvir\nname;jatt") 
 
with open ("info.txt",'r') as f :
    print(f.read())

#problem 3 
line=0
with open ("info.txt",'w')as f :
    f.write( "hello world!\niam manvir singh bhangu\nfrom village bhangwan\nits located in amritsar\nthank you everyone")
with open ("info",'r')as f :
    for i in f:
      lines=f.readlines()
line=len(lines)
word=0
char=0
for line in lines:
    word +=len(line.split())
    char+=len(line)
print("lines",line)
print("words",word)
print("char",char                     )
    
##problem 4:
with open ("student.txt",'w') as f:
    for i in range(3):
        name=input("enter name:")
        marks=int(input("enter marks:"))
        f.write(f"{name},  {marks}\n")
print("passed student :")
with open("student.txt",'r') as f:
     for line in f:
         data=line.split()
         name=data[0]
         marks=int(data[1])
         if marks>=40:
             print(f"{name},{marks}")

#problem 5 :
with open("para.txt",'w')as f :
    print("enter 5 lines:")
    for i in range(5):
        line=input()
        f.write(line+"\n")
word=input("enter word to find :")
linesfound=[]
with open("para.txt",'r') as f :
    for line_no,line in enumerate(f.readline(),start=1):
        if word in line:
            linesfound.append(line_no)
if linesfound:
    print(f"{word},found on lines:",*linesfound)
else:
    print(f"{word},not found")




        

  
    
        
        
        
