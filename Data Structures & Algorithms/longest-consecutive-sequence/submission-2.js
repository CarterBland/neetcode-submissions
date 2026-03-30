class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let best = 0;
        nums.sort((a, b) => a - b);

        const map = new Map();

        for (const num of nums) {
            if (map.has(num)) continue;

            const complement = num - 1;
            const streak = (map.get(complement) || 0) + 1

            map.set(num, streak);
            
            best = Math.max(best, streak);

            if (map.has(complement)) map.delete(complement);
        }

        return best;
    }
}
