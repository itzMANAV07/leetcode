class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        count=0
        other=[]
        for i in range(nums[0],nums[-1]):
            other.append(i)
        return list(sorted(set(other) - set(nums)))

    
        
        