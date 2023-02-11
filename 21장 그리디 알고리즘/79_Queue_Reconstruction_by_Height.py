class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for h, k in people:
            heapq.heappush(heap, (-h, k))
        
        answer = []
        while heap:
            h, k = heapq.heappop(heap)
            answer.insert(k, [-h, k])
        
        return answer
      
