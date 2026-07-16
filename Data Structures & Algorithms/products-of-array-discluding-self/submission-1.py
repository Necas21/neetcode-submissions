class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        prefix_product = 1
        for i in range(len(nums)):
            prefix_product *= nums[i]
            prefix[i] = prefix_product
        
        postfix = [1] * len(nums)
        postfix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix_product *= nums[i]
            postfix[i] = postfix_product

        for i in range(len(nums)):
            if i == 0:
                nums[i] = postfix[i + 1]
            elif i == len(nums) - 1:
                nums[i] = prefix[i - 1]
            else:
                nums[i] = prefix[i - 1] * postfix[i + 1]
            
        return nums