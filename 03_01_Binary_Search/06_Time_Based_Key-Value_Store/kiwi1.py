class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        data = self.store.get(key, [])
        data.append((timestamp, value))
        self.store.update({key: data})

    def get(self, key: str, timestamp: int) -> str:
        data = self.store.get(key, [])
        if not data:
            return ""
        l, r = 0, len(data) - 1
        if data[l][0] > timestamp:
            return ""
        if data[r][0] < timestamp:
            return data[r][1]
        while l <= r:
            c = l + (r - l) // 2
            if data[c][0] > timestamp:
                r = c - 1
            elif data[c][0] < timestamp:
                l = c + 1
            else:
                return data[c][1]
        return data[c - 1][1]
