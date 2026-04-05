class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            best = max(best, min(heights[left], heights[right]) * (right - left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return best