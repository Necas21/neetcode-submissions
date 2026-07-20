class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort nums
        nums.sort()

        result = []

        # Iterate over nums
        for i in range(len(nums) - 2):
            # Skip the same element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            # Use i, left and right pointers to track indices
            while left < right:
                # If the sums == 0 append to result
                if nums[i] + nums[left] + nums[right] == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                # If the sums < 0 we increment left to get a bigger value
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                # If sums > 0 we decrement right to get a smaller value
                else:
                    right -= 1 
        return result