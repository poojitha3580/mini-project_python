try:
    f=open("sample.txt","w")
    f.write("hello python")
except exception:
    print("error  while writing file")
finally:
    f.close()
    print("file closed successfully")