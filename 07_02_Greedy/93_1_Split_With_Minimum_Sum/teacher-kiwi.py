# 문제 요약:
# 양의 정수 num의 각 자리의 숫자를 가지고 두 개의 숫자를 만든다.
# 그렇게 만든 두 개의 숫자의 합이 최소일 때 그 값을 구하는 문제


# 첫 번째 풀이:
# 1. 각 자리의 숫자를 담은 배열 nums를 만든다.
# 2. nums를 내림차순으로 정렬한다.
# 3. nums의 요소를 차례로 보면서 두 개씩 묶어 10의 n 제곱 값을 곱하여 합을 구한다.
class Solution:
    def splitNum(self, num: int) -> int:
        nums = []
        # 각 자리의 숫자를 nums에 담는 코드
        while num > 0:
            nums.append(num % 10)
            num //= 10

        nums.sort(reverse=True)

        res = 0
        for i in range(len(nums)):
            res += nums[i] * 10 ** (i // 2)
        return res


# 결과: Runtime 28 ms Beats 79% // Memory 13.8 MB Beats 47.10%
# 평가:
# 이 코드의 시간 복잡도는 O(NlogN)이며, 공간 복잡도는 O(N)입니다.
# num을 10으로 나누고 num // 10을 수행하여 num의 각 자릿수를 얻으며, 각 반복에서 nums에 그 값을 추가하는 루프가 있습니다.
# 이 루프는 num의 자릿수 N에 비례하며, 각 반복에서 수행하는 연산의 시간 복잡도는 O(1)입니다.
# 그러나 그 이후에 nums 배열을 정렬하는 데 O(NlogN)의 시간이 걸리며, 그 이후의 반복에서는 최대 2로 나눈 i의 승인 10의 지수 연산이 수행됩니다.
# 따라서 전체 시간 복잡도는 O(NlogN) + O(N) + O(N) = O(NlogN)입니다.
# 공간 복잡도는 nums 배열에 모든 num 자릿수를 저장하므로 O(N)입니다.

#########################################################################################


# 두 번째 풀이:
# 1. 각 자리 숫자를 계수 정렬(counting sort) 한다.
# 2. 큰 수부터 하나씩 꺼내면서 base를 곱한다.
# 3. base는 곱해질 때마다 두 번에 한 번 씩 10배씩 커진다.
class Solution:
    def splitNum(self, num: int) -> int:
        nums = [0] * 10
        while num > 0:
            nums[num % 10] += 1
            num //= 10
        res, base, flag = 0, 1, True
        for i in range(9, -1, -1):
            while nums[i] > 0:
                res += i * base
                base *= 1 if flag else 10
                flag = not flag
                nums[i] -= 1
        return res


# 결과: Runtime 34 ms Beats 44.2% // Memory 14 MB Beats 8.88%
# 평가:
# 이 개선된 코드의 시간 복잡도는 O(N)입니다.
# 이유는 입력된 수의 자리수에 비례하는 반복문(for loop)이 한 번 수행되고, 그 이후에 각 자리수마다 counting sort 알고리즘이 수행되기 때문입니다.
# counting sort는 입력 크기에 비례하는 시간 복잡도를 가지므로, 전체 시간 복잡도는 O(N)입니다.
# 공간 복잡도는 입력된 수의 자리수에 비례하는 O(k)입니다.
# 이유는 counting sort를 위한 nums 배열을 생성할 때, 배열 크기를 입력된 수의 자리수에 맞춰 10으로 설정했기 때문입니다.
# 따라서 입력된 수의 자리수가 클수록 nums 배열도 커지며, 공간 복잡도도 증가합니다.
