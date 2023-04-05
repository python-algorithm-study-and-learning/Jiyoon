import collections

def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    
    deque = collections.deque([])
    for city in cities:
        city = city.lower()
        
        if city in deque:
            deque.remove(city)
            answer += 1
        else:
            if len(deque) == cacheSize:
                deque.popleft()
            answer += 5
            
        deque.append(city)
    
    return answer
    
