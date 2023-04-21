from collections import defaultdict 

nums1 = [3,4,6,5] 
nums2 = [9,1,2,5,8,3] 
k = 5

# 목표 : k 자리수를 만든다. 
#1. nums1과 nums2에서 숫자를 i, k-i개 가져옴. 
#2.  가저온 수 조합을 result에 넣음.
#1과2의 과정을 반복  

result = 0

hs = defaultdict

for i in range(len(nums2)):
    if hs[[1]] < nums2[i]:
        hs[1] = nums2[i]
    elif hs[2] < nums2[i]:
        hs[2] = nums2[i]
    elif hs[3] < nums2[i]:
        hs[3] = nums2[i]
    elif hs[4] < nums2[i]:
        hs[4] = nums2[i]

print(hs)



# 6 9583 = 96583

# 65 983 = 98653

# 465 98 = 98465

# 3465 9 = 93465
