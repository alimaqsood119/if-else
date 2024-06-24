i=0
sum=0
while(i<5):
    y=int(input("Enter a number :"))
    
    if(y<0):
        print("number is negqative ")
        break
    else:
        # y=int(y)
        sum=sum+y
        i=i+1
print("The total sum is ",sum)
        