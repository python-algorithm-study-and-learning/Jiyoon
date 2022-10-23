class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for f, t, p in flights:
            graph[f].append((t, p))
        
        queue = [(0, src, k)]
        
        while queue:
            price, node, stop = heapq.heappop(queue)
            if node == dst:
                return price
            if stop >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(queue, (alt, v, stop - 1))
                    
        return -1
