class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)

        for i in range(len(nums)):
            left[i] = left[i-1] * nums[i-1] if i != 0 else 1
            right[len(nums) - 1 - i] = right[len(nums) - i] * nums[len(nums) - i] if i != 0 else 1

        return [left[i] * right[i] for i in range(len(nums))]