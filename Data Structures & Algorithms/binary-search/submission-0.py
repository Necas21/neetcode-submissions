class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Pointers to start and end of list
        start = 0
        end = len(nums) - 1

        while start < end:
            # Calculate mid point
            mid = ((end - start) // 2) + start

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        if nums[start] == target:
            return start
        else:
            return - 1
        