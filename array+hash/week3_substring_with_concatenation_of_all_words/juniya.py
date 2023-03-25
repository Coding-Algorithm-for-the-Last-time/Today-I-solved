from collections import Counter

s = "barfoothefoobarman"
words = ["foo","bar"]

#s를 words 길이만큼으로 자르기
s = map(''.join, zip(*[iter(s)]*len(words[0])))

for i in words:
    print(Counter(i))

