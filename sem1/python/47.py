a=list(map(int,input("Enter the list of numbers : ").split()))
i=0
while i<len(a):
    if a[i]==237:
        break
    elif a[i]%2==0:
        print(a[i])
    i+=1
