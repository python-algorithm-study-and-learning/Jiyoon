class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = collections.Counter(stones)
        result = 0
        
        for jewel in jewels:
            result += count[jewel]
        return result
