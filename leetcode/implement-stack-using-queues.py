class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        self.q = deque()
        while len(self.queue) > 1:
            num = self.queue.popleft()
            self.q.append(num)
        popped = self.queue.popleft()
        while self.q:
            val = self.q.popleft()
            self.queue.append(val)
        del self.q
        return popped


    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()