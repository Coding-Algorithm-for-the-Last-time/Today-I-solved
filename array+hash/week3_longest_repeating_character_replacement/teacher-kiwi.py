from collections import deque, defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        word = deque()
        result = 0
        
        for char in s:
            cnt[char] += 1
            word.append(char)
  
            while len(word) - max(cnt.values()) > k or len(cnt) > k+1:
                char = word.popleft()
                cnt[char] -= 1
                if cnt[char] == 0:
                    cnt.pop(char)
            
            if len(word) > result:
                result = len(word)

        return result
        
    

