class Solution(object):
    def majorityElement(self, nums):
        x=nums[0]
        count=0

        for i in range(len(nums)):
            if count==0:
                x=nums[i]
            if nums[i]==x:
                count+=1
            else:
                count-=1
        return x