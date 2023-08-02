class MinStack:
    def __init__(self):
        self.li = []
        self.min = []

    def push(self, val: int) -> None:
        self.li.append(val)
        self.min.append(min(val, self.min[-1] if self.min else val))

    def pop(self) -> None:
        self.li.pop()
        self.min.pop()

    def top(self) -> int:
        return self.li[-1]

    def getMin(self) -> int:
        return self.min[-1]
