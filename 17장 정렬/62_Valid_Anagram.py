class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = collections.Counter(s)
        t_dict = collections.Counter(t)
        return s_dict == t_dict
      
