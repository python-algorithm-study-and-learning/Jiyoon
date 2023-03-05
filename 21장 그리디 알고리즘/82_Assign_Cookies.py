class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        greed_heap = []
        size_heap = []

        for greed in g:
            heapq.heappush(greed_heap, greed)
        for size in s:
            heapq.heappush(size_heap, size)

        cnt = 0
        while greed_heap and size_heap:
            greed = heapq.heappop(greed_heap)
            while size_heap:
                size = heapq.heappop(size_heap)
                if greed <= size:
                    cnt += 1
                    break

        return cnt
      
