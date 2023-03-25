class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        word_length = len(words[0])
        cs_length = word_length * len(words)
        result = []

        cnt = {}
        for word in words:
            cnt[word] = cnt.get(word, 0) + 1

        for i in range(0, len(s)+1-cs_length):
            temp = {}
            for j in range(0, cs_length, word_length):
                substring = s[i:i+cs_length][j:j+word_length]
                if substring not in cnt:
                    break
                temp[substring] = temp.get(substring, 0) + 1
                if temp[substring] > cnt[substring]:
                    break
            else:
                result.append(i)

        return result