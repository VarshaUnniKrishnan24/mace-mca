n=input("enter the numbers in list:")
n=list(map(int,n.split()))
c=[num for num in n if num>100]
print(c)
