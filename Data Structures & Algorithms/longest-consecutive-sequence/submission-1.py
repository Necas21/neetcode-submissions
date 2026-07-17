class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Deal with empty list edge case
        if len(nums) == 0:
            return 0

        # Remove duplicates
        nums_set = set(nums)

        # Sort the remaining numbers
        sorted_nums = sorted(list(nums_set))

        # Track maximum consecutive value
        max_consecutive = 1

        # Store each max_consecutive in result list
        result = []

        for i in range(1, len(sorted_nums)):
            # If the difference between 2 adjacent values is 1 then they are consecutive
            if sorted_nums[i] - sorted_nums[i - 1] == 1:
                max_consecutive += 1
            else:
                # Append current max_consecutive to result and reset max_consecutive to 1
                result.append(max_consecutive)
                max_consecutive = 1
        # Append the final max_consecutive
        result.append(max_consecutive)
        
        return max(result)