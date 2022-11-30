class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
                    
        while k > 1:
            k -= 1
            heapq.heappop(heap)
            
        return -heapq.heappop(heap)
