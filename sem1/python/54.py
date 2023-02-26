def cal(x,y):
    return(x+y,x-y,x*y,x/y)
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=cal(a,b)
print("Sum = ",c[0])
print("Difference = ",c[1])
print("Product = ",c[2])
print("Division : ",c[3])
