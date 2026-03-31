class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let bestPrice = 0;
        let lowestPoint = Infinity;

        for (let i = 0; i < prices.length; i++) {
           lowestPoint = Math.min(prices[i], lowestPoint);
           bestPrice = Math.max(bestPrice, prices[i] - lowestPoint); 
        }

        return bestPrice;
    }
}
