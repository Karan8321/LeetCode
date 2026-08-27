class Solution(object):
    def subarraySum(self, nums, k):
        Map={0:1}
        count=0
        PrefSum=0
        for i in range(len(nums)):
            PrefSum+=nums[i]
            count+=Map.get(PrefSum-k,0)
            Map[PrefSum]=Map.get(PrefSum,0)+1
        return count