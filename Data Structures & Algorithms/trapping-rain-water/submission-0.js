class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        let area = 0;
        let maxLeftHeight = 0;
        let maxRightHeight = 0;
        let left = 0;
        let right = height.length - 1;

        while (left < right) {
            maxLeftHeight = Math.max(maxLeftHeight, height[left]);
            maxRightHeight = Math.max(maxRightHeight, height[right]);

            if (height[left] < height[right]) {
                area += maxLeftHeight - height[left];
                left++;
            } else {
                area += maxRightHeight - height[right];
                right--;
            }
        }

        return area;
    }
}
