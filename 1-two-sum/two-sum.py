class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}
        for i in range(len(nums)):
            first = nums[i]
            after = target - first  
            if after in num:
                return [num[after], i]
            num[first] = i
