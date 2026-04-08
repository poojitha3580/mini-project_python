queue=[]
while True:
    print("\nQueue Operations Menu")
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Front")
    print("4.Rear")
    print("5.is Empty")
    print("6.Display")
    print("7.Exit")
    choice=int(input("enter choice:"))
    if choice==1:
        val=int(input("enter value:"))
        queue.append(val)
        print("Enqueued:",val)
    elif choice==2:
        if len(queue)==0:
            print("queue underflow")
        else:
            print("Dequeued:",queue.pop(0))
    elif choice ==3:
        if len(queue)==0:
            print("queue is empty")
        else:
            print("front element:",queue[0])
    elif choice==4:
        if len(queue)==0:
            print("queue is empty")
        else:
            print("rear element:",queue[-1])
    elif choice==5:
        print("is queue empty?",len(queue)==0)
    elif choice==6:
        print("queue:",queue)
    elif choice==7:
        break
    else:
        print("invalid choice")