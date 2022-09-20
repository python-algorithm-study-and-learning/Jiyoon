class MyHashMap:

    def __init__(self):
        self.hashmap = list()

    def put(self, key: int, value: int) -> None:
        for i, x in enumerate(self.hashmap):
            if x[0] == key:
                self.hashmap[i][1] = value
                return
        
        self.hashmap.append([key, value])

    def get(self, key: int) -> int:
        for k, v in self.hashmap:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        for i, x in enumerate(self.hashmap):
            if x[0] == key:
                del self.hashmap[i]
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
