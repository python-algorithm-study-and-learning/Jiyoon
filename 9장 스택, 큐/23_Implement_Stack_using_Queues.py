class MyStack:

    def __init__(self):
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()

    def push(self, x: int) -> None:
        if self.queue1:
            self.queue1.append(x)
        else:
            self.queue2.append(x)

    def pop(self) -> int:
        if self.queue1:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.popleft())
            return self.queue1.popleft()
        elif self.queue2:
            while len(self.queue2) > 1:
                self.queue1.append(self.queue2.popleft())
            return self.queue2.popleft()
        else:
            return None

    def top(self) -> int:
        if self.queue1:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.popleft())
            val = self.queue1.popleft()
            self.queue2.append(val)
            return val
        
        elif self.queue2:
            while len(self.queue2) > 1:
                self.queue1.append(self.queue2.popleft())
            val = self.queue2.popleft()
            self.queue1.append(val)
            return val
        else:
            return None

    def empty(self) -> bool:
        if self.queue1 or self.queue2:
            return False
        return True 


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
