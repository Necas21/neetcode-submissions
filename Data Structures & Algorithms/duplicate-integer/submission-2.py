class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()

        for n in nums:
            nums_set.add(n)
        
        return not (len(nums) == len(nums_set))
        