class Node:
    def __init__(self, key: str, data = None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:

    def __init__(self):
        self.head = Node(None)

    def insert(self, word: str) -> None:
        node = self.head
        
        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
                
            node = node.children[char]
            
        node.data = word

    def search(self, word: str) -> bool:
        node = self.head
        
        for char in word:
            if char not in node.children:
                return False
            
            node = node.children[char]
            
        return True if node.data == word else False

    def startsWith(self, prefix: str) -> bool:
        node = self.head
        
        for char in prefix:
            if char not in node.children:
                return False
            
            node = node.children[char]
        
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
