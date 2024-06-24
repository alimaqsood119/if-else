y=int(input("Enter a number :"))
while(y%2==1):
    print("The number is odd")
    y=int(input("Enter a number again :"))
print("The number",y, "is even ")
for c in range(1,11):
    print(y,"X",c,"=",y*c)