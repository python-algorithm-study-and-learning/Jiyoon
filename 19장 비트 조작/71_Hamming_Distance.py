class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bin_num = bin(x ^ y)
        return bin_num.count('1')
        
