class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        res = ""
        while word1 and word2:
            if word1[0] > word2[0]:
                res += word1[0]
                word1 = word1[1:]
            elif word1[0] < word2[0]:
                res += word2[0]
                word2 = word2[1:]               
            else:
                if word1 > word2:
                    res += word1[0]
                    word1 = word1[1:]
                else:
                    res += word2[0]
                    word2 = word2[1:]                     
        if word1:
            res += word1
        else:
            res += word2
            
        return res
    

    def largestMerge_two(self, word1: str, word2: str) -> str:
        res = ""
        
        while word1 and word2:
            if word1 > word2:
                res += word1[0]
                word1 = word1[1:]
            else:
                res += word2[0]
                word2 = word2[1:]                     
            
        return res + word1 + word2
    

    # reference : https://youtu.be/x2p3C4hEyLo