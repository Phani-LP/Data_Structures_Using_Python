#Linked list using Python
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtBegin(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        return "Node Inserted at Begining Successfully"
        
    def insertAtIndex(self,data,index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if index == position :
            print(self.insertAtBegin(data))
        else:
            while (position+1 != index and current_node != None):
                position += 1
                current_node = current_node.next
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
                return "Node inserted at the given index."
            else:
                return "Index not found."
    def insertAtEnd(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return "List is empty so node inserted at begining."
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        current_node.next = new_node
        return "Node inserted at the end successfully."
    def Display(self):
        current_node = self.head
        while(current_node):
            print(current_node.data, end = " => ")
            current_node = current_node.next
    
    
    def DeleteAtBegin(self):
        if self.head == None:
            return "Linkedlist is already empty."
        self.head = self.head.next
        return "Node at the begining deleted successfully"
    def DeleteAtEnd(self):
        if self.head == None:
            return "Linkedlist is already empty."
        current_node = self.head
        
        while(current_node.next.next):
            current_node = current_node.next
        current_node.next = None
        return "Node at the end deleted sucesfully"
        
    def DeleteAtIndex(self,index):
        position = 0
        if position == index:
            self.head = self.head.next
        else:
            current_node = self.head
            while(current_node.next != None and position+1 != index):
                position+=1
                current_node = current_node.next
            if current_node != None:
                current_node.next = current_node.next.next
                return "Node deleted successfully"
            else:
                return "Index not found."
    def LengthOfList(self):
        if self.head == None:
            return "List is empty."
        length = 1
        current_node = self.head
        while(current_node.next != None):
            length+=1
            current_node =  current_node.next
        return length
        
    
L = LinkedList()
print("1 - Insert At Begin\n2 - Insert at a index\n3 - Insert at the end\n4 - Diasply\n5 - Detele at Begin\n6 - Delete at End\n7 - Delete At Index\n8 - Length of list\n9 - Exit")
while(True):
    choice = int(input("Enter your choice 1/2/3/4/5/6/7/8/9: "))
    if choice == 1:
        data = input("Enter the data: ")
        print(L.insertAtBegin(data))
    elif choice == 2:
        data = input("Enter the data: ")
        index = int(input("Enter the index: "))
        print(L.insertAtIndex(data,index))
    elif choice == 3:
        data =input("Enter the data: ")
        print(L.insertAtEnd(data))
    elif choice == 4:
        L.Display()
    elif choice == 5:
        print(L.DeleteAtBegin())
    elif choice == 6:
        print(L.DeleteAtEnd())
    elif choice == 7:
        index = int(input("Enter the index: "))
        print(L.DeleteAtIndex(index))
    elif choice == 8:
        print(L.LengthOfList())
    elif choice == 9:
        print("Exited")
        break
    else:
        print("Invalid Choice")