class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def moving(self, key: int) -> None:
        if key == 2:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
        elif key == 1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

    def push(self, x: int) -> None:
        if self.stack2:
            self.moving(2)
            
        self.stack1.append(x)

    def pop(self) -> int:
        if self.stack1:
            self.moving(1)
            
        if self.stack2:
            return self.stack2.pop()
        else:
            return None

    def peek(self) -> int:
        if self.stack1:
            self.moving(1)
            
        if self.stack2:
            return self.stack2[-1]
        else:
            return None

    def empty(self) -> bool:
        if self.stack1 or self.stack2:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
