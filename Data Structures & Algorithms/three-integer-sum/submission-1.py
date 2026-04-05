class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        sortedNums = sorted(nums) # O(nlogn)
        
        for i, num in enumerate(sortedNums):
            if i > 0 and num == sortedNums[i - 1]:
                continue # ignore same anchors

            left = i + 1
            right = len(nums) - 1
            while left < right:
                currentSum = num + sortedNums[left] + sortedNums[right]
                if currentSum == 0:
                    leftNum = sortedNums[left]
                    rightNum = sortedNums[right]
                    results.append([num, leftNum, rightNum])

                    while left < right and sortedNums[left] == leftNum:
                        left += 1
                    while left < right and sortedNums[right] == rightNum:
                        right -= 1
                elif currentSum < 0:
                    left += 1
                else:
                    right -= 1

        return results