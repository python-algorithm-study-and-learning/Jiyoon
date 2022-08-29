# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            
        slow = slow.next
        new_head = ListNode(0)
        
        while slow:
            node = ListNode(slow.val)
            node.next, new_head = new_head, node
            
            slow = slow.next
            
        while new_head.next:
            if new_head.val != head.val:
                return False
            new_head = new_head.next
            head = head.next
        
        return True
