class Solution(object):
    def minSubArrayLen(self, target, nums):
        minLen=float('inf')
        left = 0
        window=0

        for i,v in enumerate(nums):
            window+=v
            while target<=window :
                minLen=min(i-left+1,minLen)
                window-=nums[left]
                left+=1
                
                
        return 0 if minLen==float('inf') else  minLen
