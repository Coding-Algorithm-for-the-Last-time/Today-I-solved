from collections import Counter
import math

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
       
        answer_counts = Counter(answers)

        total_rabbits = 0

        for num,count in answer_counts.items():
            if num >= count:
                total_rabbits += num+1

            else:
                total_rabbits += math.ceil(count/(num+1))*(num+1)

        return (total_rabbits)
    
#문제풀이
#1. 토끼의 대답을 counter로 dict로 만듬.
#2. 토끼의 대답(num)를 key값, count를 value값으로 하여 for문을 돌림.
#3. 토끼의 대답(num)이 count의 수보다 크거나 같으면 total_rabbit에 +1을 함.
#4. 아니면, count/ num+1을 올림한거에 (num+1)을 곱해서 total_rabbit에 더함.
# ex) 3이라고 대답한 토끼가 10마리면, 10 / (3+1) = 2.5 -> 3으로 올리고 *4를 함. 3이라고 대답한 토끼는 총 12마리있음(2마리는 대답하지 않은 토끼)
#5. total_Rabbit return 