# 225. Implement Stack using Queues

from collections import deque


class MyStack:

    def __init__(self):
        self.deq = deque()

    def push(self, x: int) -> None:
        self.deq.append(x)

    def pop(self) -> int:
        for i in range(len(self.deq)-1):
            self.push(self.deq.popleft())
        return self.deq.popleft()

    def top(self) -> int:
        return self.deq[-1]

    def empty(self) -> bool:
        return len(self.deq) == 0

        # Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
print(param_2)
param_3 = obj.top()
print(param_3)
param_4 = obj.empty()
