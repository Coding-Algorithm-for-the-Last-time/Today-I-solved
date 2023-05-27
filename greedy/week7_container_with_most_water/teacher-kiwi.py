class Solution:
    def maxArea(self, height: list[int]) -> int:
        id_height = []

        for i in range(len(height)):
            id_height.append((height[i], i))
        id_height.sort(reverse=True)

        if id_height[0][1] < id_height[1][1]:
            l, r = (id_height[0][0], id_height[0][1]), (id_height[1][0], id_height[1][1])
        else:
            r, l = (id_height[0][0], id_height[0][1]), (id_height[1][0], id_height[1][1])
        res = min(l[0], r[0]) * abs(l[1]-r[1])

        for i in range(2, len(id_height)):
            h, n = id_height[i]
            area_a = h * (abs(l[1]-n))
            area_b = h * (abs(r[1]-n))
            res = max(res, area_a, area_b)

            if l[1] > n:
                l = (h, n)
            elif r[1] < n:
                r = (h, n)

        return res