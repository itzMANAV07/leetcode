class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency={}
        for num in nums:
            if num not in frequency:
                frequency[num]=1
            else:
                frequency[num]+=1
        sorted_dict = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
        key = list(sorted_dict.keys())[0]
        return key
