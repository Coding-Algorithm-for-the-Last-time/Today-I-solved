from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 1 and len(words) == 1:
            return [0]

        word_length = len(words[0])
        li_length = len(words)
        answer = []

        for i in range(len(s) - word_length):
            per_check = s[i : i + word_length * li_length]
            if len(per_check) < word_length * li_length:
                break
            divided_word_list = self.divide_to_word_list(per_check, word_length)
            if Counter(divided_word_list) == Counter(words):
                answer.append(i)
        return answer

    def divide_to_word_list(self, per_check, length):
        return [per_check[i : i + length] for i in range(0, len(per_check), length)]
