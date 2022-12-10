class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])

        result = []

        start, end = -1, -1
        for interval in intervals:
            if start == -1:
                start, end = interval[0], interval[1]
                continue

            if interval[0] <= end:
                if end <= interval[1]:
                    end = interval[1]
                else:
                    continue
            else:
                result.append([start, end])
                start, end = interval[0], interval[1]
        
        result.append([start, end])
        
        return result
      
