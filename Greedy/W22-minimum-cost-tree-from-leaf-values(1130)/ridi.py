from typing import List

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0

        # 반복 조건    
        while len(arr) > 1:
            # arr 순회
            min = 15 * 15
            idx = 0
            for i in range(len(arr) - 1):
                val = arr[i] * arr[i+1]
                if val < min:
                    min = val
                    idx = i
            
            res += min
            if arr[idx] < arr[idx+1]:
                arr.pop(idx)
            else:
                arr.pop(idx+1)
            print(res)
            print(arr)
            print('*' * 100)

        return res
    

    def mctFromLeafValues_two(self, arr: List[int]) -> int:
        stack = [float('inf')]
        result = 0
        
        for num in arr:
            while stack[-1] <= num:
                top = stack.pop()
                result += top * min(stack[-1], num)
            stack.append(num)
        
        while len(stack) > 2:
            result += stack.pop() * stack[-1]
        
        return result