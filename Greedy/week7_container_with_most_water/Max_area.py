
# 첫번째 풀이: 시간초과
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max_area = 0

#         for i in range(len(height)):
#             for j in range(i+1, len(height)):
#                 if max_area == 0:
#                     max_area = (j - i)*(min(height[i], height[j]))
#                 elif max_area != 0:
#                     update_area = (j-i)*(min(height[i], height[j]))
#                     max_area = max(max_area, update_area)


#         return (max_area)

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         left = 0
#         right = len(height) -1
#         max_area = 0

#         while left < right:
#             h = min(height[right], height[left])
#             w = right - left
#             area = h * w
#             max_area = max(max_area, area)

#             if height[left] < height[right]:
#                 left += 1

#             else:
#                 right -=1

#         return max_area
