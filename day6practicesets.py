problem 1 

for i in range(1,51):
   
    num=i
    if num%3==0:
        print("fizz")
    elif num%5==0:
        print("buzz")
    else:
        print(i)

problem 2 

number = int(input("guess number :"))
attempts=0
secret=5
while number!=secret:
  attempts=attempts+1
  if number>secret:
        print("too high ")
  else:
        print("too low ")

  number=int(input("give ur number again :)"))
  attempts=attempts+1
print("correct")
print("attempts=",attempts)

problem3
list=[]
for i in range (5):
  numbers=int(input("what are ur numbers"))
  list.append(numbers)
  print(list)
print(sum(list))
print(max(list))
print(min(list))
average=(sum(list))/len(list)
print(average)
if list==sorted(list):
    print("srted")
else:
    print("not sorted")

problem4 
balance=(1000)
while True :
    n=int(input("\n.....menu...... "))
    print("1.deposit")
    print("2.withdrawel ")
    print("3 balance")
    print ("4.exit")
    choice=int(input("enter your choice : "))

    if choice==1:
        amount=int(input("enter your amount:"))
        balance=amount+balance
        print(balance)
    elif choice==2:
        amount=int(input("enter withdrawel "))
        if amount>balance:
            print("insufficent balance ")
        elif amount<=balance:
            balance=balance-amount
            print("balance is :",balance)
    elif choice==3:
     print("your balance is :",balance)
    else:
        print("you are exited")
    

problem 5
def main():
    n=int(input("enter your input:"))
    print_triangle(n)
def print_triangle(size):
    for i in range(size):
        for j in range(i+1):
            
            print("#",end='')
        print()
main()