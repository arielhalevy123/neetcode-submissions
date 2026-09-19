class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            start=i+1
            end=len(nums)-1
            
            while end>start:
                sum3=nums[start]+nums[i]+nums[end]
                if sum3==0:
                    res.append([nums[i],nums[start],nums[end]])
                    while start < end and nums[end]==nums[end-1] :
                        end=end-1
                    while start<end and nums[start]==nums[start+1]:
                        start=start+1
                    end =end-1
                    start=start+1
                elif sum3>0: 
                    end=end-1
                else:
                    start=start+1
                
        return res
            
            

