class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
        max_arr=[]
        for _ in range(k):
            most = max(count, key=count.get)
            max_arr.append(most)
            del count[most]
        return max_arr        
       

            