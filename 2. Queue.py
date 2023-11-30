#Lets implement the Queue - FIFO
class Queue:
    def __init__(self):
        self.items = []
    def Enqueue(self,data):
        self.items.append(data)
        return "Element inserted successfully."
    def Dequeue(self):
        if len(self.items)==0:
            return "Sorry, Queue is empty. We can't perform deletion."
        else:
            print("Deleted element is: ")
            return self.items.pop(0)
    def Display(self):
        if len(self.items)==0:
            return "Queue is empty."
        else:
            return self.items
            
P = Queue()
print("Enqueue - 1\nDequeue - 2\nDisplay - 3\nExit - 4")
while True:
    c = int(input("Enter your choice: 1 / 2 / 3 / 4: "))
    if c==1:
        data = int(input("Enter the number: "))
        P.Enqueue(data)
    elif c==2:
        print(P.Dequeue())
    elif c==3:
        print(P.Display())
    elif c==4:
        print("Program Closed")
        break
    else:
        print("Invalid choice")
