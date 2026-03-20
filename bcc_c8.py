class Node:
    def __init__(self,info):
        self.info=info
        self.link=None
class LinkedList:
    def __init__(self):
        self.start=None
    def insert(self):
        info=int(input("Enter any number:"))
        temp=Node(info)
        if self.start is None:
            self.start=temp
        else:
            t1=self.start
            while t1.link is not None:
                t1=t1.link
            t1.link=temp    
    def delete_node(self):
        if self.start is None:
            print("list is empty")
        else:
            self.start=self.start.link
    def print_list(self):
        if self.start is None:
            print("List is empty:")
        else:
            t2=self.start
            while t2 is not None:
                print(t2.info,end=" ")
                t2=t2.link
            print()
            
            
class Node:
    def __init__(self,info):
        self.info=info
        self.link=None
class LinkedList:
    def __init__(self):
        self.start=None
    def insert(self):
        info=int(input("Enter any number:"))
        temp=Node(info)
        if self.start is None:
            self.start=temp
        else:
            t1=self.start
            while t1.link is not None:
                t1=t1.link
            t1.link=temp    
    def delete_node(self):
        if self.start is None:
            print("list is empty")
        else:
            self.start=self.start.link
    def print_list(self):
        if self.start is None:
            print("List is empty:")
        else:
            t2=self.start
            while t2 is not None:
                print(t2.info,end=" ")
                t2=t2.link
            print()    
    def menu(self):
        print("1.ADD\n2.Delete\n3.Print\n4.Exit\n")
        return int(input("Enter your choice:"))
    def run(self):
        while True:
            choice=self.menu()
            if choice==1:
                self.insert()
            elif choice==2:
                self.delete_node()
            elif choice==3:
                self.print_list()
            elif choice==4:
                exit()
            else:
                print("Invalid entry")                
if __name__=="__main__":
   l1=LinkedList()  
   l1.run()
   
   
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        previous = None
        currentPOS = head   # start
        next = None

        while currentPOS is not None:
            next = currentPOS.next
            currentPOS.next = previous
            previous = currentPOS
            currentPOS = next

        return previous
    
    
class Solution(object):
    def hasCycle(self, head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
    
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self,head):
     slow=head
     fast=head
     while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            break
        else:
            return None # there is no cycle
       
   slow=head
    while  slow!=fast:
            slow=slow.next
            fast=fast.next
    return slow

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
