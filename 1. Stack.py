class Stack:
    def __init__(self):
        self.items = []
    def push(self, data):
        self.items.append(data)
        print("Data pushed succcessfully.")
    def pop(self):
        if len(self.items)==0:
            return "Stack is empty. We can't delete."
        else:
            return self.items.pop()
    def display(self):
        if len(self.items) == 0:
            return "Stack is empty"
        else:
            return self.items
p = Stack()
print("Push - 1\nPop - 2\nDisplay - 3\nExit - 4")
while True:
    c = int(input("Enter your choice: 1 / 2 / 3 / 4: "))
    if c==1:
        data = int(input("Enter the number: "))
        p.push(data)
    elif c==2:
        print(p.pop())
    elif c==3:
        print(p.display())
    elif c==4:
        break
    else:
        print("Invalid choice")
        