class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let best = 0;

        const numSet = new Set(nums);

        for (const num of nums) {
            if (!numSet.has(num - 1)) {
                let currentStreak = 1;
                while (numSet.has(num + currentStreak)) {
                    currentStreak++;
                }

                best = Math.max(currentStreak, best);
            }

            numSet.add(num);
        }

        return best;
    }
}
