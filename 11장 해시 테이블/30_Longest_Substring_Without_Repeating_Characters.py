class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == len(set(s)):
            return len(s)
        elif len(set(s)) <= 2:
            return len(set(s))
        
        answer = 0
        length = 0
        start = 0
        store = collections.defaultdict(int)
        
        for i, char in enumerate(s):
            if not store[char]:
                store[char] = i + 1
                length += 1
            else:
                start = max(store[char], start)
                store[char] = i + 1
                length = i - start + 1
                
            answer = max(answer, length)
        
        return answer
