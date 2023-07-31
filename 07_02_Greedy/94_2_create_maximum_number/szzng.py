def get_max_stack(array, k):
    stack = []
    left = len(array)-k
    if left <0 : return array

    for i, v in enumerate(array):
        while left>0 and stack and stack[-1] < v:
            stack.pop()
            left-=1
        stack.append(v)
    return stack[:k]

def merge(list1, list2):
  result = []
  while list1 or list2:
    if list1>list2:
      result.append(list1.pop(0))
    else:
      result.append(list2.pop(0))
  
  return result


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        result = []
        for i in range(k+1):
            if i>len(nums1) or k-i>len(nums2): continue
            list1 = get_max_stack(nums1, i)
            list2 = get_max_stack(nums2, k-i)
            result = max(result, merge(list1,list2))
        return result 
