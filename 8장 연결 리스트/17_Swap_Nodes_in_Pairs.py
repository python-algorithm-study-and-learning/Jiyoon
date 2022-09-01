# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = end = ListNode(0)
        end.next = head
        
        temp = head
        
        while temp and temp.next:
            node = temp.next
            
            node.next, temp.next = temp, node.next
            
            end.next = node
            end = end.next.next
            temp = temp.next
        
        return root.next
