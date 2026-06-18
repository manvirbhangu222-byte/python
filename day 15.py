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

#problem 2 : append 
with open ('info','w') as f :
    f.write('''name :manvir
            name : singh 
            name:bhangu''')
    f.close()
f=open('info','a')
f.write("name : manvir \n name ; jatt")
print(f.read())
f.close()
    
