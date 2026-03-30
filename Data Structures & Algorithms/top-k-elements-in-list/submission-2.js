class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const map = new Map();
        const bucket = Array.from({ length: nums.length + 1 }, () => []);
        const result = [];

        for (const num of nums) {
            map.set(num, (map.get(num) || 0) + 1);
        }

        for (const [num, frequency] of map.entries()) {
            bucket[frequency].push(num);
        }

        for (let i = bucket.length - 1; i >= 0; i--) {
            for (const topElement of bucket[i]) {
                result.push(topElement);
                if (result.length === k) {
                    return result;
                }
            }
        }

        return result;
    }
}
