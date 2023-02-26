a=list(input("Enter the words  : ").split(','))
b=[]
i=0
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i+=1
b.sort()
print(b)
