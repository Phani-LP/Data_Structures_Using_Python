class Node:
    def __init__(self,data):
        self.next = None
        self.data = data
        self.prev = None

class Pallavi:
    def __init__(self):
        self.head = None
    def InsertAtBegin(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return "Node inserted at the begining successfully"
        else:
            self.new_node.next = self.head
            self.head.prev = self.new_node
            self.new_node = self.head
            return "Node inserted at the begining successfully"
    def InsertAtIndex(self,data,index):
        position = 0
        new_node = Node(data)
        current_node = self.head
        if position == index:
            return self.InsertAtBegin(data)
        else:
            while(position+1 != index and current_node is not None):
                position+=1
                current_node = current_node.next
            if current_node != None:
                new_node.prev = current_node
                new_node.next = current_node.next
                if current_node.next != None:
                    current_node.next.prev = new_node
                current_node.next = new_node
                return "Node inserted at Index."
            else:
                return "Index not found."
    def InsertAtEnd(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return "List is empty so node inserted at the begining."
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            new_node.prev = current_node
            current_node.next = new_node
            return "Node inserted at End."
    def Display(self):
        pass
    def DeleteAtBegin(self):
        pass
    def DeleteAtIndex(self):
        pass
    def DeleteAtEnd(self):
        pass

DL = Pallavi()
print("1 - Insert At Begin\n2 - Insert at a index\n3 - Insert at the end\n4 - Exit")
while(True):
    choice = int(input("Enter your choice 1/2/3/4: "))
    if choice == 1:
        data = input("Enter the data: ")
        print(DL.InsertAtBegin(data))
    elif choice == 2:
        data = input("Enter the data: ")
        index = int(input("Enter the index: "))
        print(DL.InsertAtIndex(data,index))
    elif choice == 3:
        data =input("Enter the data: ")
        print(DL.InsertAtEnd(data))
    elif choice == 4:
        exit()
    else:
        print("Invalid Choice.")
