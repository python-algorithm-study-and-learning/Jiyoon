class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = collections.defaultdict(list)
        
        for s in strs:
            anagram[str(sorted(s))].append(s)
            
        return anagram.values()
