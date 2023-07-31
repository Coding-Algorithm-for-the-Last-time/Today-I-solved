class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = ""

        while word1 != "" or word2 != "": 
            if word1 < word2:
                merge += word2[0]
                word2 = word2[1:]
        
            else:
                merge += word1[0]
                word1 = word1[1:]
        
        return (merge)
    