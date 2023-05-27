# 문제 요약:
# 중복된 값이 있을 수 있는 정수 배열이 있다.
# 한 번에 특정 정수를 모두 제거할 수 있을 때, 처음 배열의 반 이하로 만들기 위한 제거할 최소 정수 개수는?


# 첫 번째 풀이:
# 1. 정수 배열에서 정수의 개수를 구한다.
# 2. 가장 많은 정수부터 차례대로 배열의 길이에서 개수만큼 뺀다.
# 3. 뺀 값이 배열의 길이가 절반 이하가 되었을 때 지금까지 뺀 횟수를 리턴한다.
class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        count = {}
        length = len(arr)

        for i in range(length):
            count[arr[i]] = count.get(arr[i], 0) + 1

        count_values = sorted(count.values(), reverse=True)
        length //= 2

        for i in range(len(count_values)):
            length -= count_values[i]
            if length <= 0:
                return i + 1


# 결과: Runtime 574 ms Beats 80.9% // Memory 32.2 MB Beats 69.56%
# 평가:
# 이 코드의 시간 복잡도는 O(nlogn)입니다.
# count 딕셔너리를 만드는데 O(n)의 시간이 걸립니다.
# count.values()를 사용하여 딕셔너리의 값들을 가져오는데 O(n)의 시간이 걸립니다.
# sorted() 함수를 사용하여 값을 내림차순으로 정렬하는데, 최악의 경우 O(nlogn)의 시간이 걸립니다.
# 마지막으로 count_values 리스트를 순회하면서 길이를 줄이는데 최대 O(n)의 시간이 걸립니다.
# 이 코드의 공간 복잡도는 O(n)입니다.
# 공간 복잡도는 count 딕셔너리를 만드는데 O(n)의 공간이 필요합니다.
# 또한, count_values 리스트도 필요하므로 O(n)의 공간이 더 필요합니다.

#############################################################################################


# 두 번째 풀이:
# 1. 정수 배열에서 정수의 개수를 구한다.
# 2. 정렬을 위한 배열을 만드는데, 길이는 주어진 배열의 반만큼한다.(정수의 개수가 절반 이상인 것이 있으면 바로 리턴!)
# 3. 정수의 개수에 해당하는 index에 1씩 올린다.(계수 정렬)
# 4. 정수의 개수가 많은 것부터 내림차순으로 빼가며, 처음 배열의 절반 이하로 떨어질 때 횟수를 리턴한다.
class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        count = {}
        length = len(arr)

        for i in range(length):
            count[arr[i]] = count.get(arr[i], 0) + 1

        length //= 2
        counting = [0] * length

        for _, cnt in count.items():
            if cnt >= length:
                return 1
            counting[cnt] += 1

        removed_cnt, size = 0, 0
        for cnt in range(length - 1, -1, -1):
            while counting[cnt] > 0:
                removed_cnt += cnt
                size += 1
                if removed_cnt >= length:
                    return size
                counting[cnt] -= 1


# 결과: Runtime 644 ms Beats 34.38% // Memory 32.3 MB Beats 61.46%
# 평가:
# 이 코드의 시간 복잡도는 O(n + klogk)이고, 공간 복잡도는 O(k)입니다.
# 여기서 n은 입력 배열 arr의 길이이고, k는 arr에서 서로 다른 숫자의 개수입니다.
# 시간 복잡도에서 O(n)은 arr에서 각 숫자의 개수를 세는 부분, O(klogk)는 counting 리스트를 역순으로 탐색하는 부분입니다.
# 공간 복잡도에서는 arr에서 서로 다른 숫자의 개수인 k만큼의 공간을 counting 리스트에 할당하고, 나머지는 상수 공간으로 O(1)입니다.
