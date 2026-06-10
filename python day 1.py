#ask user for their age 
name =input("What is your name ").strip().title()
age = input("what is your age ").strip()
first,last=name.split(" ")
print (f"your name is {last}" )
print("and age is :"+age)

