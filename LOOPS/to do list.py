task=[]
while True:
    print("\n1.add task")
    print("2.view tasks")
    print("3.exit")
    choice=input("enteer choice:")
    if choice=="1":
        task=input("enter task:")
        tasks.append(task)
        print("task added")
    elif choice=="2":
        print("your tasks:")
        for t in tasks:
            print("_",t)
    elif choice=="3":
        break
    else:
        print("invalid choice")