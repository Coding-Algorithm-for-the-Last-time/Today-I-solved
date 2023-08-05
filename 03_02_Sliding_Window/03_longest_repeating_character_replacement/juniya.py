
def max_length_substring(s, k):
    left = 0
    right = 0
    max_length = 0
    char_count = {}

    while right < len(s):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        # char_count에 A또는 B의 빈도수를 딕셔너리로 입력
        max_count = max(char_count.values())
        # CHAR_COUNT의 값 중 가장 빈도수가 높은 값을 저장
        if right - left +1 - max_count > k:
            #만약 윈도우의 크기에서 최빈도의 값을 뺐는데 K보다 크다면 왼쪽 인덱스를 이동시킴
            char_count[s[left]] -=1
            left +=1
        
        max_length = max(max_length, right - left +1 )
        #가장 긴 길이와 윈도우의 크기를 비교하여 더 큰 거를 가장 긴 길이로 저장
        
        right +=1
        #포인터를 오른쪽으로 한칸 이동

    return max_length

