class Node:
    def __init__(self, key: int = 0, val: int = 0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"Node(val={self.val}, prev={self.prev})"


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap: dict[int, Node] = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        self.update(key)
        return self.hashmap[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.update(key)
            self.hashmap[key].val = value
            return
        if self.capacity == len(self.hashmap):
            self.delete()
        self.append(key, value)

    def delete(self):
        temp = self.tail.prev
        temp.prev.next = self.tail
        self.tail.prev = temp.prev
        self.hashmap.pop(temp.key)

    def append(self, key: int, value: int):
        node = Node(key, value)
        self.head.next.prev = node
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        self.hashmap[key] = node

    def update(self, key: int):
        self.hashmap[key].prev.next = self.hashmap[key].next
        self.hashmap[key].next.prev = self.hashmap[key].prev
        self.hashmap[key].next = self.head.next
        self.hashmap[key].prev = self.head
        self.head.next = self.hashmap[key]
        self.hashmap[key].next.prev = self.hashmap[key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
