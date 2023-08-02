class MinStack:
    def __init__(self):
        self.li = []

    def push(self, val: int) -> None:
        self.li.append(val)

    def pop(self) -> None:
        self.li.pop()

    def top(self) -> int:
        return self.li[-1]

    def getMin(self) -> int:
        if not self.li:
            return None
        _min = self.li[0]
        for s in self.li:
            _min = min(_min, s)
        return _min
