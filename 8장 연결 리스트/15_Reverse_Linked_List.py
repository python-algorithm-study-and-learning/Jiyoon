# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        
        while head:
            node = ListNode(head.val)
            node.next, new_head = new_head, node
            
            head = head.next
        
        return new_head
