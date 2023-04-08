class Solution:
    def balancedStringSplit(self, s: str) -> int:
        right = 0
        check_LR = {"R": 0, "L": 0}
        count = 0 

        while right < len(s):
            if s[right] == next(iter(check_LR)):
                #next(iter(check_LR))대신에 list(check_LR.keys())[0] 가능
                check_LR["R"] += 1

            else:
                check_LR["L"] += 1

            if check_LR["R"] == check_LR["L"]:
                count +=1

            right +=1

        return count 


#슬라이딩 윈도우 알고리즘을 이용
#right가 전체 길이에 도달할때까지 while문 사용
#s의 첫번째가 check딕셔너리의 첫번째 키값과 같다면 아니면 L을 올림
