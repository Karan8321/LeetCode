class Solution(object):
    def minSubArrayLen(self, target, nums):
        window=0
        minLen=float('inf')
        left=0

        for right in range(len(nums)):
            window+=nums[right]
            while target<=window:
                minLen=min(minLen,right-left+1)
                window-=nums[left]
                left+=1
            
        return minLen if minLen!=float('inf') else 0
        