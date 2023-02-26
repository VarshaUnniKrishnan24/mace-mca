class validate(Exception):pass
try:
    username="merin1602"
    password="m@r!n16*2"
    u=input("Enter Username  : ")
    p=input("Enter Password : ")
    if u!=username or p!=password:
        raise validate("Invalid login credentials")
    else:
        print("Login Success")
except validate as e:
    print(e)
