a=input("enter the number ")
print(f"multiplication table of {a}is :")
try:
    for i in range(1,11):
        print(f"{int (a)} x {i}= {int(a)*i}")
except:
    print("invalid input ")
try:
    num=int(input("what is your number :"))
    a=[5,6]
    print(a[num])
except ValueError:
    print("input is wrong ")
except IndexError:
    print("index is wrong : ")
    