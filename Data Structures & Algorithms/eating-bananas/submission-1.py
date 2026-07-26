class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1 <= k <= max(piles)
        min_k = 1
        max_k = max(piles)
        mid_k = ((max_k - min_k) // 2) + min_k

        # Tracks the slowest value of k to get below h
        slowest_k = max_k

        while min_k <= max_k:
            # Mid speed
            mid_k = ((max_k - min_k) // 2) + min_k
            
            # Reset time_to_eat
            time_to_eat = 0

            # Calculate time to eat all bananas
            for i in range(len(piles)):
                time_to_eat += math.ceil(piles[i] / mid_k)
            
            # Move max and min pointers
            if time_to_eat > h:
                min_k = mid_k + 1
            else:
                max_k = mid_k - 1
                slowest_k = min(slowest_k, mid_k)
            
        return slowest_k