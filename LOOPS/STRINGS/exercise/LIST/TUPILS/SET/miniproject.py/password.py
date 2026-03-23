def check_password(password):
    if len(password)>=8:
        print("strong password")
    else:
        print("weak password")
check_password("Olive$123")    