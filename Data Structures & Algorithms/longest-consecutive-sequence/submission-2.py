class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Deal with empty list edge case
        if len(nums) == 0:
            return 0

        # Remove duplicates
        nums_set = set(nums)

        # Store results
        result = []

        for n in nums_set:
            start_seq = n
            consecutives = 1
            # Find the start of the sequence
            while True:
                if (start_seq - 1) in nums_set:
                    start_seq -= 1
                else:
                    break
            # Find the length of the sequence
            while True:
                if (start_seq + 1) in nums_set:
                    consecutives += 1
                    start_seq += 1
                else:
                    result.append(consecutives)
                    break
        return max(result)



