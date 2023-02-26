import math
a=int(input("First number:"))
b=int(input("Last number:"))
for i in range(a,b):
    if int(math.sqrt(i))**2==i:
        t=i
        while t>0:
            if (t%10)%2!=0:
                break
            t=int(t/10)
        else:
            print(i)
    
