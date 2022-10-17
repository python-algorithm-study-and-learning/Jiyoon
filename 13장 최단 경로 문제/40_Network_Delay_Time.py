class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def dijkstra(start:int):
            distances = {node: float("inf") for node in range(1, n + 1)}
            distances[start] = 0
            queue = []
            heapq.heappush(queue, [distances[start], start])
            
            while queue:
                cur_dist, cur_place = heapq.heappop(queue)
                
                if distances[cur_place] < cur_dist:
                    continue
                    
                for new_place, new_dist in graph[cur_place].items():
                    dist = cur_dist + new_dist
                    if dist < distances[new_place]:
                        distances[new_place] = dist
                        heapq.heappush(queue, [dist, new_place])
                        
            return distances
        
        graph = collections.defaultdict(dict)
        for u, v, w in times:
            graph[u][v] = w
        
        result = max(dijkstra(k).values())
        return -1 if result == float("inf") else result
