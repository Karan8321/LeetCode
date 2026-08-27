class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        def atMost(k):
            Hmap={}
            count=0
            left=0
            for i in range(len(nums)):
                Hmap[nums[i]]=Hmap.get(nums[i],0)+1
                while Hmap and len(Hmap)>k:
                    Hmap[nums[left]]-=1
                    if Hmap[nums[left]]==0:
                        del Hmap[nums[left]]
                    left+=1
                count+=i-left+1
            return count
        return atMost(k)-atMost(k-1)


        