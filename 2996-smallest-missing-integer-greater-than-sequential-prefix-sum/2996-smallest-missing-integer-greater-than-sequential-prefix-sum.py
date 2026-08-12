class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        s = nums[0]
        for i in range(1, n):
            if nums[i] != nums[i - 1] + 1:
                break
            s += nums[i]
        while s in nums:
            s += 1
            
        return s
