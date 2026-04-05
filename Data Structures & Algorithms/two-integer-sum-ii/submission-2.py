class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            numSum = numbers[left] + numbers[right]
            if numSum == target:
                return [left+1, right+1]
            elif numSum < target:
                left += 1
            elif numSum > target:
                right -= 1

        return [] # should never hit