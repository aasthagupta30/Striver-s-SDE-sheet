class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min, max_so_far = prices[0], 0
        for price in prices:
            current_min = min(current_min,  price)
            max_so_far = max(max_so_far, price-current_min)
        return max_so_far
        
