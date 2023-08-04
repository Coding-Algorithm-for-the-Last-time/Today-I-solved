class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = []
        for i in range(len(position)):
            count = target - position[i] / speed[i]
            cars.append((position[i], count))
        cars.sort(key=lambda x: x[0], reverse=True)
        maxV = 0
        res = 0
        for car in cars:
            if car[1] > maxV:
                maxV = car[1]
                res += 1
        return res
