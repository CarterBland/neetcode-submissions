class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        numFrequencies = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            numFrequencies[num] = numFrequencies.get(num, 0) + 1
        
        for num, frequency in numFrequencies.items():
            buckets[frequency].append(num)
        
        for i in range(len(buckets)):
            for j in buckets[len(buckets) - 1 - i]:
                result.append(j)

                if len(result) == k:
                    return result
                
        return result