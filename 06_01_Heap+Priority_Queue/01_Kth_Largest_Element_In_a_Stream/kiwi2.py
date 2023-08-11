class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        dummy = ListNode(0)
        temp = dummy
        for num in sorted(nums, reverse=True):
            temp.next = ListNode(num)
            temp = temp.next
        self.nums = dummy.next

    def add(self, val: int) -> int:
        dummy = ListNode(0)
        dummy.next = self.nums
        node = dummy
        while node and node.next:
            if val > node.next.val:
                temp = ListNode(val)
                temp.next = node.next
                node.next = temp
                break
            node = node.next
        else:
            node.next = ListNode(val)

        self.nums = dummy.next
        temp = self.nums
        for _ in range(self.k - 1):
            temp = temp.next

        return temp.val


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
