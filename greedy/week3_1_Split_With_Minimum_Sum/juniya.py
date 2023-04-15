from collections import Counter

class Solution:
    def splitNum(self, num: int) -> int:
        freq = Counter(str(num))

        num1 =""
        num2 =""

        keys = sorted(freq.keys())

        while sum(freq.values()) > 0:
            for i in keys:
                if freq[i] >0:
                    num1 += i
                    freq[i] -= 1
                    break

            for i in keys:
                if freq[i] >0:
                    num2 += i
                    freq[i] -= 1
                    break

        return int(num1) + int(num2)
    

#문제풀이 
#1. num을 문자열로 바꾸면서 Counter를 이용해서 각 문자열의 출현 횟수를 기록한 dict를 만듬
#2. 내림차순으로 정렬함
#3. 가장 횟수가 많은 숫자부터 내림차순으로 num1에 추가하고 출현횟수를 -1함. 출현횟수가 0이 될떄까지 num2와 번갈아가면서 추가함
#4. 그다음 숫자를 3번 과정을 반복함. freq.values()의 합이 0이 되면 while문 종료
#5. num1과 num2를 int로 변환하고 return함
