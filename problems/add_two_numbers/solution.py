# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        extra = None
        finres = None
        pointer = None
        
        while True:
            
            if(l1==None and l2==None):
                # carry = 0
                break
            
            
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0
            
            
            temp = l1_val + l2_val + carry
            carry = 0
            
            if(temp>=10):
                carry,temp = str(temp) 
                carry = int(carry)
                temp = int(temp)
            # print(carry,temp)
                

            if(finres == None):
                finres = ListNode(temp)
                pointer = finres
                
            else:
                pointer.next = ListNode(temp)
                pointer =  pointer.next
                
                    
            
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        
        
        pointer = finres
        
        while pointer.next!=None:
            pointer = pointer.next
        
        if(carry>0):
            
            pointer.next = ListNode(carry)
        
        return finres