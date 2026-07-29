class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Left and right pointers
        left = 0
        right = len(nums) - 1

        # Current minimum
        curr_min = min(nums[left], nums[right])

        while left <= right:
            curr_min = min(nums[left], nums[right], curr_min)
            left += 1
            right -= 1
        
        return curr_min