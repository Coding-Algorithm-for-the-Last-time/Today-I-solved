
def max_length_substring(s, k):
    left = 0
    right = 0
    max_length = 0
    char_count = {}

    while right < len(s):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        max_count = max(char_count.values())
        if right - left +1 - max_count > k:
            char_count[s[left]] -=1
            left +=1
        
        max_length = max(max_length, right - left +1 )
        right +=1

    return max_length


s = "AABABBA"
k = 1

max_length_substring(s, k)