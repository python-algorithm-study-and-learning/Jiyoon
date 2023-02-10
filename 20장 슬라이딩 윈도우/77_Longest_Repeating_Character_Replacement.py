class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        answer = 0
        counts = collections.Counter(s[0])
        for right in range(1, len(s)):
            counts[s[right]] += 1
            
            common_char = counts.most_common(1)[0][1]
            if right - left + 1 - common_char > k:
                counts[s[left]] -= 1
                left += 1
            else:
                answer = max(answer, right - left + 1)
        return answer
        
