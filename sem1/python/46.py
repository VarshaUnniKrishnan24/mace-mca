a=list(map(int,input("Enter list of numbers:").split()))
b=int(input("Enter item to search:"))
i=count=0
while i<len(a):
    if a[i]==b:
        count+=1
    i+=1
if count==0:
    print("Item not found")
else:
    print("Item found",count,"times")
