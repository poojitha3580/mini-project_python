try:
    username=input("enter username:")
    password =input("enter password:")
    if username =="admin" and password =="234":
        print("login successful")
    elif username=="" or passwor=="":
        raise ValueError("Empty input not allowed")
    else:
        print("invalid credentials")
except ValueError as e:
    print("Error:",e)
finally:
    print("completed")