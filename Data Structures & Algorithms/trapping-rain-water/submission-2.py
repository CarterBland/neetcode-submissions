class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height) - 1
        maxLeft = 0
        maxRight = 0

        while left < right:
            maxLeft = max(height[left], maxLeft)
            maxRight = max(height[right], maxRight)

            if height[left] < height[right]:
                maxLeft = max(maxLeft, height[left])
                area += maxLeft - height[left]
                left += 1
            else:
                maxRight = max(maxRight, height[right])
                area += maxRight - height[right]
                right -= 1

        return area