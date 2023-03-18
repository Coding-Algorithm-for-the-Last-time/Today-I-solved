class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        id_dict, anagrams = {}, []

        for word in strs:
            key = "".join(sorted(word))
            if key in id_dict:
                anagrams[id_dict[key]].append(word)
            else:
                id_dict[key] = len(anagrams)
                anagrams.append([word])

        return anagrams