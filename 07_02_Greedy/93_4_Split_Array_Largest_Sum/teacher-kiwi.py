# 문제 요약:
# int가 들어있는 nums배열을 k개로 나누어 각각의 부분 배열의 합 중에서 최대값을 구한다.
# k개로 나누는 방법은 여러 가지이므로 앞에서 구한 값 여러 개 중에서 최소값을 리턴한다.


# 첫 번째 풀이:
# 1. nums의 부분합X -> 누적합을 구한다.(부분 배열의 합을 빨리 구하기 위해)
# 2. nums를 k개로 나눌 수 있는 모든 경우의 수를 찾는다.
# 3. 각각의 경우에서 부분 배열의 합 중 최대값을 찾는다.
# 4. 그 중에 최소값을 리턴한다.
class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        length = len(nums)

        # 부분합을 구하는 부분
        partial_sum = [0]
        for i in range(length):
            partial_sum.append(nums[i] + partial_sum[i])

        # 결과는 항상 배열의 모든 수를 더한 값보다 작으므로 일단 모든 수를 더한 값을 넣어둔다.
        # 함수 안에서 res 변수값을 바꾸기 위해 클래스 멤버 변수로 만든다.
        self.res = partial_sum[-1]

        # nums를 k개로 나눌 수 있는 모든 부분 배열을 찾고 부분 배열의 합의 최대값 중 최소값을 찾는 함수
        def get_max_sum_subarray(start, end, k, max_sum_subarray):
            # k를 줄여가다가 k가 1이 되면, 남은 부분 배열이 하나이므로 남는 부분이 마지막 부분 배열이 된다.
            if k == 1:
                # 마지막 부분 배열의 합을 구하는 코드
                last_sum_subarray = partial_sum[-1] - partial_sum[start]
                # 지금까지 찾은 부분 배열의 합의 최대값이 최소인 값을 res에 저장한다.
                self.res = min(self.res, max(max_sum_subarray, last_sum_subarray))

            elif start < end:
                # 마지막에 빈 배열을 부분 배열로 구하는 것을 막기 위해 end-1까지만 loop
                for i in range(start, end - 1):
                    # 첫 번째 부분 배열의 합을 구한다.
                    current_sum_subarray = partial_sum[i + 1] - partial_sum[start]
                    # k값을 1씩 줄여가면서 나머지 부분 배열의 합을 구하기 위해 재귀적으로 함수를 호출한다.
                    # 부분 배열의 합 중 최대값을 넘겨준다.
                    get_max_sum_subarray(
                        i + 1, end, k - 1, max(max_sum_subarray, current_sum_subarray)
                    )

        get_max_sum_subarray(0, length, k, 0)

        return self.res


# 결과: 시간 초과
# 평가:
# 모든 경우의 수를 찾는 건 비효율적이다.
# 부분 배열의 합을 빨리 찾으려고 부분합을 사용했는데, 문제를 해결할 핵심적인 알고리즘이 모든 경우의 수를 찾는 게 아니다.

# 이 코드의 시간 복잡도는 O(n^2 log n)이다.
# get_max_sum_subarray 함수가 재귀적으로 호출되며, 이 함수에서 for loop가 length-1번 돌기 때문이다.
# 따라서 이 함수의 시간 복잡도는 O(n^2)이 된다.

# 공간 복잡도는 O(n)이다.
# 이 코드에서 nums 배열과 같은 크기의 partial_sum 배열이 추가로 필요하다.
# 따라서 공간 복잡도는 O(n)이 된다.

#########################################################################################################


# 두 번째 풀이:
# 1. 부분 배열의 합 중 최대값이 될 수 있는 범위는 배열의 요소 중 가장 큰 값 ~ 배열의 모든 요소의 합이다.
# 2. 부분 배열의 합 중 최대값이 될 수 있는 경우의 중간값을 구한다.
# 3. 부분 배열의 합 중 최대값이 중간값보다 작으면서 k개로 배열을 나눌 수 있는지 확인한다.
# 4. 3번의 결과에 따라 부분 배열의 합 중 최대값이 될 수 있는 범위를 중간값을 이용하여 반으로 줄인다.
# 5. 계속해서 반으로 줄여나가다 보면 부분 배열의 합 중 최대값이 최소가 되는 값이 나오고 그걸 리턴한다.
class Solution:
    # 3번 과정을 수행하는 함수
    def splitArray(self, nums: list[int], k: int) -> int:
        def can_split(mid):
            count = 1
            current_sum = 0
            for num in nums:
                current_sum += num
                if current_sum > mid:
                    count += 1
                    if count > k:
                        return False
                    current_sum = num
            return True

        # 1번 과정에 따라 답이 될 수 있는 범위를 할당한다.
        left, right = max(nums), sum(nums)

        # 범위를 더 줄일 수 없는 상황(left == right)이 될 때까지 반복한다.
        while left < right:
            # 2번 과정을 수행하는 코드
            mid = (left + right) // 2

            # 중간값보다 작은, 부분 배열의 합 중 최대값이 나오게 k개로 나눌 수 있다면
            if can_split(mid):
                # 범위의 최대값을 중간값으로 줄인다.
                right = mid
            else:
                # k개로 나누는 게 불가능하다면 범위의 최소값을 중간값+1로 늘린다.
                left = mid + 1

        return left


# 결과: Runtime 40ms Beats 69.9% // Memory 13.9MB Beats 65.1%
# 평가: 이진 탐색은 빠르다.

# 이 코드의 시간복잡도는 O(N log M)입니다.
# 여기서 N은 nums 배열의 길이이며, M은 nums 배열의 모든 원소들의 합입니다.
# 이는 이진 탐색에서 mid 값을 찾기 위해 O(log M) 시간이 걸리고, 이를 can_split() 함수에 대입하여 O(N) 시간이 걸리기 때문입니다.

# 공간복잡도는 O(1)입니다.
# 이진 탐색에 사용되는 변수 3개와 can_split() 함수에 사용되는 변수 3개를 제외하면, 추가적인 공간이 필요하지 않기 때문입니다.
