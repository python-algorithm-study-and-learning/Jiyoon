class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        
        left = 0
        right = 1
        for i in range(0, len(s) - 1):
            even_left, even_right = self.isPalindrome(s, i, i + 1)
            odd_left, odd_right = self.isPalindrome(s, i, i + 2)
            
            if even_right - even_left > right - left:
                left = even_left
                right = even_right
            if odd_right - odd_left > right - left:
                left = odd_left
                right = odd_right
            
        return s[left:right]
        
    def isPalindrome(self, s: str, left: int, right: int) -> list:
        if left < 0 or right >= len(s):
            return [left+1, right]
        
        if s[left] == s[right]:
            return self.isPalindrome(s, left - 1, right + 1)
        else:
            return [left+1, right]
