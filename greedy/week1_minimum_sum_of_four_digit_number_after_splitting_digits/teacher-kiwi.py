class Solution:
    def minimumSum(self, num: int) -> int:
        # 1, 2, 3, 4라고 했을 때,
        # (1, 2), (3, 4)로 작은 두 자리 수를 만든다.
        # (1, 3), (2, 4)로 작은 두 자리 수를 만든다.
        # 둘 중에 작은 것을 리턴한다.
        return min(
            min(num // 1000, num // 100 % 10) * 10
            + max(num // 1000, num // 100 % 10)
            + min(num // 10 % 10, num % 10) * 10
            + max(num // 10 % 10, num % 10),
            min(num // 1000, num // 10 % 10) * 10
            + max(num // 1000, num // 10 % 10)
            + min(num // 100 % 10, num % 10) * 10
            + max(num // 100 % 10, num % 10),
        )


##########################################################


class Solution:
    def minimumSum(self, num: int) -> int:
        # num을 문자열로 만든 뒤 정렬한다.
        # 작은 수 두 개를 십의 자리로,
        # 큰 수 두 개를 일의 자리로 만든다.
        # 두 수를 더해서 리턴
        num = sorted(str(num))
        return int(num[0] + num[2]) + int(num[1] + num[3])
