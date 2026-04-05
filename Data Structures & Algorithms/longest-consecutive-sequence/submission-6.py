class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        numSet = set(nums)

        for num in numSet:
            if num-1 in numSet:
                continue

            offset = 1
            
            while (num + offset) in numSet:
                offset += 1

            best = max(best, offset)
        
        return best
