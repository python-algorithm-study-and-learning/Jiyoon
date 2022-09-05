# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cnt = 1
        root = ListNode(0, head)
        
        left_end = root
        right_first = None
        
        reverse_head = reverse_end = None
        
        while cnt < left:
            left_end, head = head, head.next
            cnt += 1
            
        while left <= cnt <= right:
            # 역순으로 연결 시작
            node = head
            node.next, head = reverse_head, head.next
            
            reverse_head = node
            
            if cnt == left:
                reverse_end = node
            
            if cnt == right:
                reverse_end.next = head
                left_end.next = reverse_head
                
            cnt += 1
                
        return root.next
                
