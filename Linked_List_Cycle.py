# Input : Head Of the Linked List
# Output : True or False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Corner Case
        
        #Emty List
        if head is None :
            return False
        #Emty Only one Node
        elif head.next is None :
            return False
        
        hare = head
        turtel = head
        
        while hare and turtel and turtel.next:
            hare = hare.next
            turtel = turtel.next.next
            
            if hare == turtel:
                return True
            
        # If No Loop return Null         
        if hare != turtel:
            return False
        