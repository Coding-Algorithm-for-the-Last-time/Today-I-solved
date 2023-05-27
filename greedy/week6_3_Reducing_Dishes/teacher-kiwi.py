class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction.sort()
        records = [0]
        for n in satisfaction:
            temp = [0]
            for i in range(1, len(records)):
                temp.append(max(records[i], records[i - 1] + n * i))
            records = temp + [records[-1] + n * len(records)]
        return max(records)


##################################################################


class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction.sort(reverse=True)
        res = 0
        for i in range(len(satisfaction)):
            d = sum(satisfaction[: i + 1])
            if d < 0:
                return res
            else:
                res += d
        return res
