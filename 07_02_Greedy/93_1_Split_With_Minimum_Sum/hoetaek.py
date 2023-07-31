

class Solution:
    def splitNum(self, num: int) -> int:
        num_li = self.num_to_sorted_list(num)
        two_num_li = self.combine_to_two_num(num_li)
        print(two_num_li)
        return sum(two_num_li)

    def num_to_sorted_list(self, num):
        li = []
        while num > 0:
            digit = num % 10
            num = num // 10
            li.append(digit)
        return list(sorted(li))

    def combine_to_two_num(self, num_li):
        two_num_li = [0, 0]

        get_or_default = lambda li, index, default: li[index] if index < len(li) else default

        for i in range(0, len(num_li), 2):
            for j in range(len(two_num_li)):
                num = get_or_default(num_li, i+j, 0)
                if num != 0:
                    two_num_li[j] = two_num_li[j] * 10 + num

        return two_num_li

# Runtime 22 ms Beats 97.91% Memory 13.8 MB Beats 46.99%
