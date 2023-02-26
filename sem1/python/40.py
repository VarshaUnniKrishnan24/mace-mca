a=int(input("enter number of lines:"))
for i in range(a):
    for j in range(i+1):
        print("*",end='')
    print()
for i in range(a-1,0,-1):
    for j in range(i):
        print("*",end='')
    print()
