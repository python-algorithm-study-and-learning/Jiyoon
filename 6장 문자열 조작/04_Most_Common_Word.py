class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub('[^0-9a-z]', ' ', paragraph).split()
        without_ban = [x for x in paragraph if x not in banned]
        count = collections.Counter(without_ban)
        
        return count.most_common(1)[0][0]
