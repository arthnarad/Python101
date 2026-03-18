# set logic
def security_key(number):
    visible=set()
    repeatednumber=0
    for ch in str(number):
        if ch in visible:
            repeatednumber += 1
        else:
            visible.add(ch)
    return repeatednumber if repeatednumber>0 else -1
number=int(input("Enter your number"))
print(security_key(number))


class Solution:
    def middleNode(self, head):
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
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