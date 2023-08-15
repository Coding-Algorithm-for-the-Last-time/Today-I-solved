class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        data = self.store.get(key, [])
        data.append((timestamp, value))
        self.store.update({key: data})

    def get(self, key: str, timestamp: int) -> str:
        data = self.store.get(key, [])
        res = ""
        l, r = 0, len(data) - 1
        while l <= r:
            c = l + (r - l) // 2
            if data[c][0] <= timestamp:
                res = data[c][1]
                l = c + 1
            else:
                r = c - 1
        return res
