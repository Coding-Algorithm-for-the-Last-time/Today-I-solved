from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        result = 0
        freq = Counter(arr)
        sorted_freq = sorted(freq.values(), reverse=True) 
        sum_of_subarray = 0

        for v in sorted_freq:
            sum_of_subarray += v
            result += 1
            if sum_of_subarray >= (len(arr)//2):
                break

        return (result)


#문제풀이
#1. array의 요소의 출현횟수를 Counter를 이용하여 dict 만든다.
#2. 횟수가 제일 많은 숫자부터 내림차순으로 하고 합계를 변수로 만든다.
#3. for문을 돌린다. 가장 횟수가 많은 v를 sum_subarray에 추가하고 result를 1개 올린다. 만약 sum_of_subarray가 len(arr)//2보다 커지만 break한다.
#4. result를 return. 여기서 result는 몇번 요소를 제거했는가를 의미.

