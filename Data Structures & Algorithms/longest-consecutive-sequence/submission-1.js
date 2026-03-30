class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        if (nums.length === 0) return 0;

        nums.sort((a, b) => a - b);

        const map = new Map();

        for (const num of nums) {
            const complement = num - 1;
            
            if (map.has(num)) continue;
            map.set(num, (map.get(complement) || 0) + 1);
            if (map.has(complement)) map.delete(complement);
        }

        return [...map.values()].sort((a,b) => b-a)[0]
    }
}
