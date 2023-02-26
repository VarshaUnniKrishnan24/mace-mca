a=int(input("Enter number:"))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(i*j,end='\t')
    print()
