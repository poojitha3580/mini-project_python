queue=[10,20,30]
if len(queue)==0:
    print("Queue underflow!cannot dequeue")
else:
    removed = queue.pop(0)
    print("Dequeued element:",removed)
print("Queue after Dequeue:",queue)