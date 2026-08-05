class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        left=0
        prod=1
        count=0

        for right in range(len(nums)):
            prod=prod*nums[right]
            while prod>=k and left<len(nums):
                prod=prod//nums[left]
                left+=1
            count+=right-left+1

            
        return count 