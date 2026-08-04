class Solution(object):
    def twoSum(self, nums, target):
        Map={}


        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in Map:
                return [Map[complement],i]
            Map[nums[i]]=i
        