class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        total = len(nums)
        count=0
        for i in range (total):
            for j in range (1,total):
                if nums[i]+nums[j]==target and i!=j :
                    return [i,j]