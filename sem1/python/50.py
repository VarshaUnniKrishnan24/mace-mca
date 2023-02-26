a=list(input("Enter the sentance : ").split())
i=count=0
while i<len(a):
    if i<len(a[i])>=2 and (a[i][0].lower()==a[i][-1].lower()):
        count+=1
    i+=1
print("Count : ",count)
