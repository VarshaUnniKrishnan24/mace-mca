r=int(input("enter number of lines needed:"))
for i in range(1,r+1):
        print("*"*i,end="")
        print(" "*(r-i)*2,end="")
        print("*"*i)
for i in range(r,0,-1):
        print("*"*i,end="")
        print(" "*(r-i)*2,end="")
        print("*"*i)
