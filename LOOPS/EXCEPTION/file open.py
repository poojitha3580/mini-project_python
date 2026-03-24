try:
    f=open("data.txt","r")
    content=f.read()
    print(content)
except FileNotFoundError:
    print("error:",FileNotFound)
finally:
    try:
        f.close()
        print("File closed successfully")
    except:
        print("file was nott opened")