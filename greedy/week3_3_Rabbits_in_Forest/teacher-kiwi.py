# 문제 요약:
# 일부 토끼가 자신과 같은 색을 가진 토끼가 몇 마리 더 있는지 대답한다.
# 존재가 확실한 토끼는 최소 몇 마리인지 구한다.


# 첫 번째 풀이:
# 1. 토끼들의 대답을 count한다.
# 2. 최소 같은 대답(정수)에 + 1(자신) 마리 수만큼은 존재하므로, count에서 빼면서 누적합을 구한다.
# 3. count가 남아있으면 반복하고, 이 과정을 모든 대답에 반복한다.
class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        answer_count = {}
        for i in range(len(answers)):
            answer_count[answers[i]] = answer_count.get(answers[i], 0) + 1

        rabbits = 0
        for answer, count in answer_count.items():
            while count > 0:
                same_color_rabbits = answer + 1
                count -= same_color_rabbits
                rabbits += same_color_rabbits

        return rabbits


# 결과: Runtime 39 ms Beats 90.4% // Memory 13.9 MB Beats 91.70%
# 평가:
# 이 코드의 시간 복잡도는 O(n)입니다.
# 입력 리스트의 길이에 비례하여 for 루프가 2번 실행되므로 O(n)입니다.
# 이후 while 루프도 상수 시간 안에 끝나므로 영향이 없습니다.
# 공간 복잡도는 입력 리스트에서 나타날 수 있는 답변 종류의 수에 비례합니다.
# 입력 리스트에서 나타날 수 있는 답변의 최대 개수는 1000이므로 이 코드의 공간 복잡도는 O(1000)이지만, 답변의 종류 수에 비례하므로 O(k)라고 할 수 있습니다.
# 여기서 k는 답변 종류 수를 의미합니다.
