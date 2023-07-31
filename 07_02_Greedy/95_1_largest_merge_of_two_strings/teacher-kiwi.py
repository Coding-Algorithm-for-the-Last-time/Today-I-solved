class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        merged_word = ""
        while len(merged_word) < len(word1 + word2):
            if word1[i:] > word2[j:]:
                merged_word += word1[i]
                i += 1
            else:
                merged_word += word2[j]
                j += 1
        return merged_word


# Runtime 156 ms Beats 20.66% // Memory 14.1 MB Beats 80.75%
# 시간복잡도 O(N), 공간 복잡도는 O(N)
