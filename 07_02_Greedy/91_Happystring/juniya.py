class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        dic = {"a": a, "b": b, "c": c}
        res = []

        while True:
            temp = {k:v for k, v in dic.items() if v > 0}
            if not temp:
                break

            max_key = max(temp, key= temp.get)
            if len(res) > 1 and res[-2] == max_key and res[-1] == max_key:
                temp.pop(max_key)

                if not temp:
                    break

                max_key = max(temp, key= temp.get)
                res.append(max_key)
                dic[max_key] -=1

            else:
                res.append(max_key)
                dic[max_key] -= 1


        return ("".join(res))