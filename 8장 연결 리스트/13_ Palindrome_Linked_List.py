# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        
        new_head = ListNode(0)
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            
            node = ListNode(slow.val)
            node.next, new_head = new_head, node
            
            slow = slow.next
            
        if fast.next:
            node = ListNode(slow.val)
            node.next, new_head = new_head, node
        
        slow = slow.next
        
        while new_head.next:
            if new_head.val != slow.val:
                return False
            new_head = new_head.next
            slow = slow.next
        
        return True
