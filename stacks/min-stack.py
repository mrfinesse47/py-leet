class MinStack:

    def __init__(self):
        self.arr = []
        self.min = []  # keep a second stack to track min

    def push(self, val: int) -> None:
        if len(self.arr) < 1:
            self.arr.append(val)
            self.min.append(val)
        else:
            end = len(self.min) - 1
            self.min.append(min(self.min[end], val))
            self.arr.append(val)

    def pop(self) -> None:
        self.arr.pop()
        self.min.pop()

    def top(self) -> int:
        return self.arr[len(self.arr) - 1]

    def getMin(self) -> int:
        return self.min[len(self.arr) - 1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # return -3
minStack.pop()
print(minStack.top())  # return 0
print(minStack.getMin())  # return -2
