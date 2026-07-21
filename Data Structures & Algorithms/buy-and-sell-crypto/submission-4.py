class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit: int = 0

        # Initialise cheapest buy
        cheapest = prices[0]

        # Iterate over prices
        for price in prices:
            # If the current price is <= cheapest, we update cheapest
            if price < cheapest:
                cheapest = price
            # If current price - cheapest makes a greater profit than max_profit, update max_profit
            if price - cheapest > max_profit:
                max_profit = price - cheapest
        
        return max_profit