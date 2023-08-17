from collections import deque, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        q = deque()

        t_count = defaultdict(int)
        for i in t:
            t_count[i] += 1

        s_count = defaultdict(int)

        i = 0

        minWindow = ""
        minWindowLen = len(s)

        for j in range(len(s)):
            if s[j] in t_count:
                s_count[s[j]] += 1
                q.append(j)
            while self.is_b_in_a(s_count, t_count) and q:
                i = q[0]
                if minWindowLen >= j - i + 1:
                    minWindow = s[i:j + 1]
                    minWindowLen = len(minWindow)
                
                left = q.popleft()
                s_count[s[left]] -= 1

        return minWindow

    def is_b_in_a(self, a:dict, b:dict):
        for i in b:
            if i not in a:
                return False
            if b[i] > a[i]:
                return False
        return True