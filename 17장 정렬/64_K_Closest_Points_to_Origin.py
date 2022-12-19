class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getDistance(point: List) -> List:
            x, y = point[0], point[1]
            return (x**2 + y**2, point)
        
        distances = list(map(getDistance, points))
        heapq.heapify(distances)
        
        result = [heapq.heappop(distances)[1] for _ in range(k)]
        return result
      
